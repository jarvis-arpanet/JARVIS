from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI(
    title="JARVIS Home API",
    version="0.1"
)

PICO_NODES = {
    "office": "http://192.168.68.158/status"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "service": "JARVIS Home API",
        "status": "online"
    }


@app.get("/api/devices")
def get_devices():

    devices = {}

    for name, url in PICO_NODES.items():

        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()

            data = response.json()

            data["online"] = True

            devices[name] = data

        except Exception as error:

            devices[name] = {
                "device": name,
                "online": False,
                "error": str(error)
            }

    return devices
