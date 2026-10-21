#!/usr/bin/env python3
from pathlib import Path
import re
import shutil

HERE = Path(__file__).resolve().parent
MAIN = HERE / "main.py"
BACKUP = HERE / "main.py.before-history-range-update"

if not MAIN.exists():
    raise SystemExit(f"Could not find {MAIN}")

source = MAIN.read_text(encoding="utf-8")

if "hours: float = 24" in source and "bucket_minutes: int = 1" in source:
    print("History range update already installed.")
    raise SystemExit(0)

history_function = r'''# ============================================================
# Read device history
# ============================================================

def get_device_history_from_db(
    device,
    hours=24,
    bucket_minutes=1
):
    hours = max(0.25, min(float(hours), 24 * 31))
    bucket_minutes = max(1, min(int(bucket_minutes), 60))
    bucket_seconds = bucket_minutes * 60
    time_modifier = f"-{hours} hours"

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT
                MIN(collected_at) AS collected_at,
                AVG(temperature_c) AS temperature_c,
                AVG(humidity_pct) AS humidity_pct,
                MIN(sensor_ok) AS sensor_ok,
                CAST(AVG(wifi_rssi) AS INTEGER) AS wifi_rssi,
                MAX(uptime_s) AS uptime_s
            FROM sensor_readings
            WHERE
                device = ?
                AND datetime(collected_at) >= datetime('now', ?)
            GROUP BY
                CAST(strftime('%s', collected_at) AS INTEGER) / ?
            ORDER BY collected_at ASC
            """,
            (device, time_modifier, bucket_seconds),
        ).fetchall()

    result = []
    calibrator = globals().get("apply_calibration")

    for row in rows:
        raw_temperature = row["temperature_c"]
        raw_humidity = row["humidity_pct"]
        temperature = raw_temperature
        humidity = raw_humidity
        calibrated = False

        if callable(calibrator):
            try:
                calibrated_values = calibrator(
                    device,
                    raw_temperature,
                    raw_humidity
                )

                if isinstance(calibrated_values, tuple):
                    if len(calibrated_values) >= 2:
                        temperature = calibrated_values[0]
                        humidity = calibrated_values[1]
                    calibrated = (
                        bool(calibrated_values[2])
                        if len(calibrated_values) >= 3
                        else True
                    )
                elif isinstance(calibrated_values, dict):
                    temperature = calibrated_values.get(
                        "temperature_c", raw_temperature
                    )
                    humidity = calibrated_values.get(
                        "humidity_pct", raw_humidity
                    )
                    calibrated = bool(
                        calibrated_values.get("calibrated", True)
                    )
            except Exception as error:
                print(
                    f"[WARN] History calibration failed for "
                    f"{device}: {error}"
                )

        result.append({
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

    return result


'''

history_route = r'''@app.get("/api/history/{device}")
def get_device_history(
    device: str,
    hours: float = 24,
    bucket_minutes: int = 1
):
    hours = max(0.25, min(hours, 24 * 31))
    bucket_minutes = max(1, min(bucket_minutes, 60))

    return get_device_history_from_db(
        device,
        hours,
        bucket_minutes
    )
'''

function_pattern = re.compile(
    r"# ============================================================\n"
    r"# Read device history\n"
    r"# ============================================================\n\n"
    r"def get_device_history_from_db\(.*?"
    r"(?=# ============================================================\n# Poll one Pico)",
    flags=re.S,
)

if not function_pattern.search(source):
    raise SystemExit(
        "Could not locate get_device_history_from_db(); no changes made."
    )

updated = function_pattern.sub(history_function, source, count=1)

route_pattern = re.compile(
    r'@app\.get\("/api/history/\{device\}"\)\n'
    r"def get_device_history\(.*\Z",
    flags=re.S,
)

if not route_pattern.search(updated):
    raise SystemExit(
        "Could not locate /api/history/{device}; no changes made."
    )

updated = route_pattern.sub(history_route + "\n", updated, count=1)

shutil.copy2(MAIN, BACKUP)
MAIN.write_text(updated, encoding="utf-8")

print("Updated backend/main.py")
print(f"Backup: {BACKUP}")
print("Run: python -m py_compile backend/main.py")
