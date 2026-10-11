# JARVIS Pico W – Build, Upload and Stable IP Setup

This guide covers the normal workflow after changing the Pico W firmware in PlatformIO.

## 1. Edit the firmware

The shared room-node firmware is:

```text
JARVIS/
└── pico/
    └── room_node/
        ├── platformio.ini
        ├── include/
        │   ├── secrets.h
        │   └── secrets.example.h
        └── src/
            └── main.cpp
```

The real Wi-Fi credentials should remain in:

```text
include/secrets.h
```

and should be ignored by Git.

Each room is selected using a PlatformIO environment from `platformio.ini`:

```text
kitchen
main_bedroom
front_room
arthurs_room
```

## 2. Open the PlatformIO project

In VS Code, open this folder as the PlatformIO project:

```text
S:\GitHub\JARVIS\pico\room_node
```

PlatformIO should then show the four environments under **Project Tasks**.

You can also open a PlatformIO terminal using:

```text
Ctrl + Shift + P
```

then select:

```text
PlatformIO: New Terminal
```

## 3. Build the firmware

After changing `main.cpp`, build the firmware first.

### Kitchen

```powershell
pio run -e kitchen
```

### Main Bedroom

```powershell
pio run -e main_bedroom
```

### Front Room

```powershell
pio run -e front_room
```

### Arthur's Room

```powershell
pio run -e arthurs_room
```

A successful build ends with:

```text
SUCCESS
```

Building checks the code without changing the Pico.

## 4. Upload the firmware

Connect the Pico W by USB.

Upload the firmware for the room you are programming.

### Kitchen

```powershell
pio run -e kitchen -t upload
```

### Main Bedroom

```powershell
pio run -e main_bedroom -t upload
```

### Front Room

```powershell
pio run -e front_room -t upload
```

### Arthur's Room

```powershell
pio run -e arthurs_room -t upload
```

The room identity is compiled into the firmware, so the same source file can be used for every Pico.

## 5. Open the serial monitor

After uploading:

```powershell
pio device monitor -b 115200
```

Example output:

```text
============================
JARVIS Pico W Room Node
============================
Device name: kitchen
Connecting to WiFi....
WiFi connected
IP address: 192.168.68.158
MAC address: 28:CD:C1:12:34:56
HTTP server started
Status endpoint: http://192.168.68.158/status
============================
```

Exit the serial monitor with:

```text
Ctrl + C
```

If nothing appears, reset or power-cycle the Pico while the serial monitor is open.

## 6. Add the MAC address to the firmware output

To make DHCP reservations easy, print the Pico W MAC address after Wi-Fi connects.

Add this after the IP address is printed:

```cpp
Serial.print("MAC address: ");
Serial.println(WiFi.macAddress());
```

Example:

```text
Device name: kitchen
IP address: 192.168.68.158
MAC address: 28:CD:C1:12:34:56
```

Record the MAC address for each Pico.

Suggested allocation:

```text
Kitchen        -> 192.168.68.151
Main Bedroom   -> 192.168.68.152
Front Room     -> 192.168.68.153
Arthur's Room  -> 192.168.68.154
JARVIS Pi      -> 192.168.68.156
```

## 7. Create DHCP reservations on the router

Do **not** hard-code the IP address into the Pico firmware unless necessary.

Instead, log into the router and look for a menu such as:

```text
DHCP Reservation
Address Reservation
Static DHCP
Reserved IP
LAN DHCP
```

Create a reservation using the Pico's MAC address.

Example:

```text
28:CD:C1:12:34:56 -> 192.168.68.151
```

This means the Kitchen Pico still uses DHCP, but the router will always give it the same address.

After creating the reservation, reboot or power-cycle the Pico.

## 8. Verify the stable address

Open the serial monitor again:

```powershell
pio device monitor -b 115200
```

Confirm the Pico receives the reserved address.

Then test its HTTP endpoint in a browser:

```text
http://192.168.68.151/status
```

or from another machine:

```bash
curl http://192.168.68.151/status
```

Expected JSON:

```json
{
  "device": "kitchen",
  "sensor_ok": true,
  "temperature_c": 19.9,
  "humidity_pct": 57.9,
  "relays": [false, false, false, false],
  "wifi_rssi": -73,
  "uptime_s": 21
}
```

## 9. Normal development workflow

The normal sequence is:

```text
Edit code
   ↓
Build
   ↓
Upload
   ↓
Serial monitor
   ↓
Test /status
   ↓
Commit to Git
```

For the Kitchen node:

```powershell
pio run -e kitchen
pio run -e kitchen -t upload
pio device monitor -b 115200
```

Then verify:

```text
http://192.168.68.151/status
```

## 10. Commit the code to Git

Once the firmware is working:

```powershell
git status
git add .
git commit -m "Add Pico MAC address reporting"
git push
```

Before committing, make sure `secrets.h` is still ignored:

```powershell
git check-ignore -v pico/room_node/include/secrets.h
```

It should return a matching `.gitignore` rule.

Never commit the real Wi-Fi password.

## 11. Recommended next step

Once all four Pico W nodes have reserved addresses, update the Raspberry Pi hub so it knows about:

```text
Kitchen        192.168.68.151
Main Bedroom   192.168.68.152
Front Room     192.168.68.153
Arthur's Room  192.168.68.154
```

The Raspberry Pi can then poll each `/status` endpoint on a fixed schedule and store the readings centrally in SQLite.
