#include <Arduino.h>
#include <WiFi.h>
#include <DHT.h>

#include "secrets.h"

#ifndef JARVIS_DEVICE_NAME
#define JARVIS_DEVICE_NAME "unknown_room"
#endif


// ============================
// Hardware configuration
// ============================

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);


// ============================
// JARVIS configuration
// ============================

const char* DEVICE_NAME = JARVIS_DEVICE_NAME;

WiFiServer server(80);


// ============================
// Wi-Fi connection
// ============================

void connectWiFi() {

    Serial.print("Connecting to WiFi");

    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println("WiFi connected");

    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());

    Serial.print("Device: ");
    Serial.println(DEVICE_NAME);
}


// ============================
// Status endpoint
// ============================

void sendStatus(WiFiClient& client) {

    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    bool sensor_ok =
        !(isnan(humidity) || isnan(temperature));

    String json = "{";

    json += "\"device\":\"";
    json += DEVICE_NAME;
    json += "\",";

    json += "\"sensor_ok\":";
    json += sensor_ok ? "true" : "false";
    json += ",";

    json += "\"temperature_c\":";
    json += sensor_ok ? String(temperature, 1) : "null";
    json += ",";

    json += "\"humidity_pct\":";
    json += sensor_ok ? String(humidity, 1) : "null";
    json += ",";

    // Placeholder until relay board is fitted
    json += "\"relays\":[false,false,false,false],";

    json += "\"wifi_rssi\":";
    json += WiFi.RSSI();
    json += ",";

    json += "\"uptime_s\":";
    json += millis() / 1000;

    json += "}";


    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: application/json");
    client.println("Connection: close");

    client.print("Content-Length: ");
    client.println(json.length());

    client.println();
    client.print(json);
}


// ============================
// 404 response
// ============================

void sendNotFound(WiFiClient& client) {

    client.println("HTTP/1.1 404 Not Found");
    client.println("Content-Type: text/plain");
    client.println("Connection: close");
    client.println();

    client.println("JARVIS endpoint not found");
}


// ============================
// Setup
// ============================

void setup() {

    Serial.begin(115200);

    delay(1000);

    Serial.println();
    Serial.println("============================");
    Serial.println("JARVIS Pico W Room Node");
    Serial.println("============================");

    Serial.print("Device name: ");
    Serial.println(DEVICE_NAME);

    dht.begin();

    connectWiFi();

    server.begin();

    Serial.println("HTTP server started");

    Serial.print("Status endpoint: http://");
    Serial.print(WiFi.localIP());
    Serial.println("/status");

    Serial.print("MAC address: ");
    Serial.println(WiFi.macAddress());

    Serial.println("============================");
}


// ============================
// Main loop
// ============================

void loop() {

    // Reconnect if Wi-Fi drops
    if (WiFi.status() != WL_CONNECTED) {
        Serial.println("WiFi connection lost");
        connectWiFi();
    }

    WiFiClient client = server.accept();

    if (!client) {
        return;
    }

    client.setTimeout(1000);

    String request = client.readStringUntil('\r');

    if (request.indexOf("GET /status") >= 0) {

        sendStatus(client);

    } else {

        sendNotFound(client);
    }

    client.stop();
}