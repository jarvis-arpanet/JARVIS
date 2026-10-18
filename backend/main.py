import asyncio
import sqlite3

from contextlib import asynccontextmanager
from pathlib import Path

import httpx

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# ============================================================
# Configuration
# ============================================================

POLL_INTERVAL_SECONDS = 60


PICO_NODES = {
    "arthurs_room": "http://192.168.68.100/status",
    "main_bedroom": "http://192.168.68.122/status",
    "front_room": "http://192.168.68.123/status",
    "kitchen": "http://192.168.68.178/status",
    "bar": "http://192.168.68.125/status",
    "main_room": "http://192.168.68.107/status",
    "gym": "http://192.168.68.136/status",
    "lilys_room": "http://192.168.68.129/status",
}


# ============================================================
# Sensor calibration
#
# Raw readings remain untouched in SQLite. Calibration is
# applied only when readings are returned through the API.
#
# corrected = raw + offset
# ============================================================

SENSOR_CALIBRATION = {
    "arthurs_room": {
        "temperature": -0.4,
        "humidity": 2.6,
    },
    "bar": {
        "temperature": 0.0,
        "humidity": -1.2,
    },
    "front_room": {
        "temperature": 0.8,
        "humidity": 0.0,
    },
    "gym": {
        "temperature": 0.8,
        "humidity": -2.7,
    },
    "kitchen": {
        "temperature": 0.2,
        "humidity": -0.5,
    },
    "main_room": {
        "temperature": -1.8,
        "humidity": 6.1,
    },

    # Deliberately left uncalibrated until more comparison data
    # is collected / the sensor is replaced if necessary:
    # "lilys_room"
    # "main_bedroom"
}


def apply_calibration(device, temperature, humidity):
    calibration = SENSOR_CALIBRATION.get(device)

    if not calibration:
        return temperature, humidity, False

    corrected_temperature = temperature
    corrected_humidity = humidity

    if temperature is not None:
        corrected_temperature = round(
            temperature + calibration.get("temperature", 0.0),
            1
        )

    if humidity is not None:
        corrected_humidity = humidity + calibration.get("humidity", 0.0)
        corrected_humidity = max(0.0, min(100.0, corrected_humidity))
        corrected_humidity = round(corrected_humidity, 1)

    return corrected_temperature, corrected_humidity, True


# ============================================================
# Paths
# ============================================================

BACKEND_DIR = Path(__file__).resolve().parent
JARVIS_DIR = BACKEND_DIR.parent

DB_PATH = JARVIS_DIR / "data" / "jarvis.db"


# ============================================================
# Database setup
# ============================================================

def initialise_database():

    DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sensor_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                device TEXT NOT NULL,

                collected_at TEXT NOT NULL
                    DEFAULT (
                        strftime(
                            '%Y-%m-%dT%H:%M:%fZ',
                            'now'
                        )
                    ),

                temperature_c REAL,
                humidity_pct REAL,

                sensor_ok INTEGER NOT NULL
                    DEFAULT 0,

                wifi_rssi INTEGER,
                uptime_s INTEGER,

                relay_1 INTEGER NOT NULL
                    DEFAULT 0,

                relay_2 INTEGER NOT NULL
                    DEFAULT 0,

                relay_3 INTEGER NOT NULL
                    DEFAULT 0,

                relay_4 INTEGER NOT NULL
                    DEFAULT 0
            )
            """
        )


        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS device_latest (
                device TEXT PRIMARY KEY,

                updated_at TEXT NOT NULL
                    DEFAULT (
                        strftime(
                            '%Y-%m-%dT%H:%M:%fZ',
                            'now'
                        )
                    ),

                temperature_c REAL,
                humidity_pct REAL,

                sensor_ok INTEGER NOT NULL
                    DEFAULT 0,

                wifi_rssi INTEGER,
                uptime_s INTEGER,

                relay_1 INTEGER NOT NULL
                    DEFAULT 0,

                relay_2 INTEGER NOT NULL
                    DEFAULT 0,

                relay_3 INTEGER NOT NULL
                    DEFAULT 0,

                relay_4 INTEGER NOT NULL
                    DEFAULT 0,

                online INTEGER NOT NULL
                    DEFAULT 0
            )
            """
        )


        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
                idx_sensor_readings_device
            ON sensor_readings(device)
            """
        )


        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
                idx_sensor_readings_collected_at
            ON sensor_readings(collected_at)
            """
        )


        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS
                idx_sensor_readings_device_time
            ON sensor_readings(
                device,
                collected_at
            )
            """
        )


        conn.commit()


# ============================================================
# Save successful Pico reading
# ============================================================

def save_reading(data):

    relays = data.get(
        "relays",
        [False, False, False, False]
    )

    relays = list(relays) + [
        False,
        False,
        False,
        False
    ]

    relays = relays[:4]

    device = data.get("device")

    if not device:
        raise ValueError(
            "Pico response did not contain a device name"
        )


    with sqlite3.connect(DB_PATH) as conn:

        # ----------------------------------------------------
        # Historical reading
        # ----------------------------------------------------

        conn.execute(
            """
            INSERT INTO sensor_readings (
                device,
                temperature_c,
                humidity_pct,
                sensor_ok,
                wifi_rssi,
                uptime_s,
                relay_1,
                relay_2,
                relay_3,
                relay_4
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                device,

                data.get(
                    "temperature_c"
                ),

                data.get(
                    "humidity_pct"
                ),

                1 if data.get(
                    "sensor_ok"
                ) else 0,

                data.get(
                    "wifi_rssi"
                ),

                data.get(
                    "uptime_s"
                ),

                1 if relays[0] else 0,
                1 if relays[1] else 0,
                1 if relays[2] else 0,
                1 if relays[3] else 0,
            ),
        )


        # ----------------------------------------------------
        # Latest state
        # ----------------------------------------------------

        conn.execute(
            """
            INSERT INTO device_latest (
                device,
                updated_at,
                temperature_c,
                humidity_pct,
                sensor_ok,
                wifi_rssi,
                uptime_s,
                relay_1,
                relay_2,
                relay_3,
                relay_4,
                online
            )
            VALUES (
                ?,
                strftime(
                    '%Y-%m-%dT%H:%M:%fZ',
                    'now'
                ),
                ?, ?, ?, ?, ?, ?, ?, ?, ?,
                1
            )

            ON CONFLICT(device)

            DO UPDATE SET

                updated_at =
                    strftime(
                        '%Y-%m-%dT%H:%M:%fZ',
                        'now'
                    ),

                temperature_c =
                    excluded.temperature_c,

                humidity_pct =
                    excluded.humidity_pct,

                sensor_ok =
                    excluded.sensor_ok,

                wifi_rssi =
                    excluded.wifi_rssi,

                uptime_s =
                    excluded.uptime_s,

                relay_1 =
                    excluded.relay_1,

                relay_2 =
                    excluded.relay_2,

                relay_3 =
                    excluded.relay_3,

                relay_4 =
                    excluded.relay_4,

                online = 1
            """,
            (
                device,

                data.get(
                    "temperature_c"
                ),

                data.get(
                    "humidity_pct"
                ),

                1 if data.get(
                    "sensor_ok"
                ) else 0,

                data.get(
                    "wifi_rssi"
                ),

                data.get(
                    "uptime_s"
                ),

                1 if relays[0] else 0,
                1 if relays[1] else 0,
                1 if relays[2] else 0,
                1 if relays[3] else 0,
            ),
        )


        conn.commit()


# ============================================================
# Mark device offline
# ============================================================

def mark_device_offline(device):

    with sqlite3.connect(DB_PATH) as conn:

        conn.execute(
            """
            INSERT INTO device_latest (
                device,
                updated_at,
                online
            )

            VALUES (
                ?,
                strftime(
                    '%Y-%m-%dT%H:%M:%fZ',
                    'now'
                ),
                0
            )

            ON CONFLICT(device)

            DO UPDATE SET

                online = 0,

                updated_at =
                    strftime(
                        '%Y-%m-%dT%H:%M:%fZ',
                        'now'
                    )
            """,
            (device,),
        )


        conn.commit()


# ============================================================
# Read latest states from SQLite
# ============================================================

def get_latest_devices_from_db():

    with sqlite3.connect(DB_PATH) as conn:

        conn.row_factory = sqlite3.Row

        rows = conn.execute(
            """
            SELECT
                device,
                updated_at,
                temperature_c,
                humidity_pct,
                sensor_ok,
                wifi_rssi,
                uptime_s,
                relay_1,
                relay_2,
                relay_3,
                relay_4,
                online

            FROM device_latest

            ORDER BY device
            """
        ).fetchall()

    devices = {}

    for row in rows:
        raw_temperature = row["temperature_c"]
        raw_humidity = row["humidity_pct"]

        temperature, humidity, calibrated = apply_calibration(
            row["device"],
            raw_temperature,
            raw_humidity,
        )

        devices[row["device"]] = {
            "device": row["device"],
            "updated_at": row["updated_at"],
            "temperature_c": temperature,
            "humidity_pct": humidity,
            "raw_temperature_c": raw_temperature,
            "raw_humidity_pct": raw_humidity,
            "calibrated": calibrated,
            "sensor_ok": bool(row["sensor_ok"]),
            "wifi_rssi": row["wifi_rssi"],
            "uptime_s": row["uptime_s"],
            "relays": [
                bool(row["relay_1"]),
                bool(row["relay_2"]),
                bool(row["relay_3"]),
                bool(row["relay_4"]),
            ],
            "online": bool(row["online"]),
        }

    return devices


# ============================================================
# Read device history
# ============================================================

def get_device_history_from_db(
    device,
    limit=100
):

    with sqlite3.connect(DB_PATH) as conn:

        conn.row_factory = sqlite3.Row

        rows = conn.execute(
            """
            SELECT
                collected_at,
                temperature_c,
                humidity_pct,
                sensor_ok,
                wifi_rssi,
                uptime_s

            FROM sensor_readings

            WHERE device = ?

            ORDER BY collected_at DESC

            LIMIT ?
            """,
            (device, limit),
        ).fetchall()

    history = []

    for row in rows:
        raw_temperature = row["temperature_c"]
        raw_humidity = row["humidity_pct"]

        temperature, humidity, calibrated = apply_calibration(
            device,
            raw_temperature,
            raw_humidity,
        )

        history.append({
            "collected_at": row["collected_at"],
            "temperature_c": temperature,
            "humidity_pct": humidity,
            "raw_temperature_c": raw_temperature,
            "raw_humidity_pct": raw_humidity,
            "calibrated": calibrated,
            "sensor_ok": bool(row["sensor_ok"]),
            "wifi_rssi": row["wifi_rssi"],
            "uptime_s": row["uptime_s"],
        })

    return history


# ============================================================
# Poll one Pico
# ============================================================

async def poll_device(client, name, url):
    try:
        response = await client.get(url, timeout=5.0)
        response.raise_for_status()

        data = response.json()

        data["device"] = name
        data["online"] = True

        save_reading(data)

        print(
            f"[OK] {name}: "
            f"{data.get('temperature_c')} C, "
            f"{data.get('humidity_pct')} %, "
            f"RSSI {data.get('wifi_rssi')} dBm"
        )

    except Exception as error:
        mark_device_offline(name)

        print(
            f"[ERROR] {name}: "
            f"{error}"
        )

# ============================================================
# Poll every Pico
# ============================================================

async def poll_all_devices():

    async with httpx.AsyncClient() as client:

        while True:

            print(
                "\n--- JARVIS device poll ---"
            )


            await asyncio.gather(
                *[
                    poll_device(
                        client,
                        name,
                        url
                    )

                    for name, url
                    in PICO_NODES.items()
                ]
            )


            print(
                "Poll complete. "
                f"Waiting "
                f"{POLL_INTERVAL_SECONDS} "
                "seconds."
            )


            await asyncio.sleep(
                POLL_INTERVAL_SECONDS
            )


# ============================================================
# FastAPI startup / shutdown
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    initialise_database()


    print(
        "Starting JARVIS "
        "background collector..."
    )

    print(
        f"Database: {DB_PATH}"
    )


    polling_task = asyncio.create_task(
        poll_all_devices()
    )


    yield


    print(
        "Stopping JARVIS "
        "background collector..."
    )


    polling_task.cancel()


    try:

        await polling_task

    except asyncio.CancelledError:

        pass


# ============================================================
# FastAPI
# ============================================================

app = FastAPI(
    title="JARVIS Home API",
    version="0.3",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ============================================================
# API routes
# ============================================================

@app.get("/")
def root():

    return {
        "service":
            "JARVIS Home API",

        "status":
            "online",

        "poll_interval_seconds":
            POLL_INTERVAL_SECONDS,

        "configured_nodes":
            len(PICO_NODES),
    }


@app.get("/api/devices")
def get_devices():

    return (
        get_latest_devices_from_db()
    )


@app.get("/api/history/{device}")
def get_device_history(
    device: str,
    limit: int = 100
):

    # Prevent accidentally asking SQLite
    # for millions of rows.
    limit = max(
        1,
        min(
            limit,
            10080
        )
    )


    return (
        get_device_history_from_db(
            device,
            limit
        )
    )