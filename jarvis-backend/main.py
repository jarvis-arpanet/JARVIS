from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

PICO_NODES = {
    "office": "http://192.168.68.158/status"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/devices")
def get_devices():
    results = {}

    for name, url in PICO_NODES.items():
        try:
            r = requests.get(url, timeout=2)
            results[name] = r.json()
            results[name]["online"] = True
        except Exception as e:
            results[name] = {
                "device": name,
                "online": False,
                "error": str(e)
            }

    return results
