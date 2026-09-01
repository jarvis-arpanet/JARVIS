# JARVIS

Local home automation and IoT platform.

## Components

- Raspberry Pi 3 hub
- FastAPI backend
- React dashboard
- Raspberry Pi Pico W room nodes
- Temperature and humidity monitoring
- Relay control
- Alexa integration

## Architecture

Pico W devices provide local sensor and control endpoints.

The Raspberry Pi acts as the central JARVIS hub, providing:

- Device polling
- API
- Data storage
- React dashboard
- Future MQTT services
