/*
 * 
 * update on 20/08/2018
 * add the LDR for the hallway light sensor
 */

#include "DHT.h"
#define DHTPIN 2     // what digital pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
DHT dht(DHTPIN, DHTTYPE);

#include <Ethernet.h>                                            //Load Ethernet Library
#include <EthernetUdp.h>                                         //Load the Udp Library
#include <SPI.h>                                                 //Load SPI Library
#include "Wire.h"                                                //imports the wire library
#include <math.h>                                                //imports the math library for the temperature calc.
#include "EmonLib.h"                                             // Include Emon Library

// ethernet
byte mac[] ={ 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEB};               //Assign mac address
IPAddress ip(192, 168, 1, 210);                                   //Assign the IP Adress
unsigned int localPort = 5000;                                   //Assign a port to talk over
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];                       //dimensian a char array to hold our data packet
String datReq;                                                   //String for our data
int packetSize;                                                  //Size of the packet
EthernetUDP Udp;                                                 //Create a UDP Object

float tempC;   
// analogue pins
/*
const int analogInPin0 = A0;                    // energy monitor 1
const int analogInPin1 = A1;                    // energy monitor 2
const int analogInPin2 = A2;                    // energy monitor 3
const int analogInPin3 = A3;                    // energy monitor 4
const int analogInPin4 = A4;                    // 
const int analogInPin5 = A5;                    // light sensor
const int analogInPin6 = A6;                    // 
const int analogInPin7 = A7;                    // 
const int analogInPin8 = A8;                    // 
const int analogInPin8 = A9;                    // 
*/
const int analogInPin5 = A5;                    // Light sensor
const int analogInPin10 = A10;                  // hallway motion 2
const int analogInPin11 = A11;                  // hallway motion 1
const int analogInPin12 = A12;                  // cold water
const int analogInPin13 = A13;                  // hot water
const int analogInPin14 = A14;                  // day element
const int analogInPin15 = A15;                  // night element

// digital pins
int lights = 22;
int bulkhead_lights = 23;
int internal_lights = 4;

// declare variables
EnergyMonitor emon1;                                             // Create an instance
EnergyMonitor emon2;
EnergyMonitor emon3;
EnergyMonitor emon4;

int HallMotion1 = 0;
int HallMotion2 = 0;

int HallwayLight = 0;

int HotWater = 0;
int ColdWater = 0;
int DayElement = 0;
int NightElement = 0;

double Thermistor(int RawADC) {
  double Temp;
  Temp = log(10000.0*((1024.0/RawADC-1))); 
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
  Temp = Temp - 273.15;            // Convert Kelvin to Celcius
  return Temp;
}
 
void setup() {
  
  Serial.begin(9600);                                             //Initialize Serial Port 
  Ethernet.begin( mac, ip);                                       //Inialize the Ethernet
  Udp.begin(localPort);                                           //Initialize Udp
  delay(1500);                                                    //delay

  emon1.current(A0, 33.3);             // Current: input pin, calibration.
  emon2.current(A1, 33.3);             // Current: input pin, calibration.
  emon3.current(A2, 33.3);             // Current: input pin, calibration.
  emon4.current(A3, 33.3);

  pinMode(lights, OUTPUT);
  pinMode(bulkhead_lights, OUTPUT);
  pinMode(internal_lights, OUTPUT);
  
  digitalWrite(lights, HIGH);
  digitalWrite(bulkhead_lights, HIGH);
  digitalWrite(internal_lights, LOW);

  dht.begin();
}
 
void loop() {

  float Irms1 = emon1.calcIrms(1480);  // Calculate Irms only
  float Irms2 = emon2.calcIrms(1480);
  float Irms3 = emon3.calcIrms(1480);
  float Irms4 = emon4.calcIrms(1480);

  HallMotion1 = analogRead(analogInPin11);
  HallMotion2 = analogRead(analogInPin10);

  HallwayLight = analogRead(analogInPin5);

  HotWater = int(Thermistor(analogRead(analogInPin12)));
  ColdWater = int(Thermistor(analogRead(analogInPin13)));
  DayElement = int(Thermistor(analogRead(analogInPin14)));
  NightElement = int(Thermistor(analogRead(analogInPin15)));
  
  packetSize = Udp.parsePacket();                                  //Reads the packet size
  
  if(packetSize>0) {                                              //if packetSize is >0, that means someone has sent a request
    
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);               //Read the data request
    String datReq(packetBuffer);                                  //Convert char array packetBuffer into a string called datReq

// ======================================================================================================
    if (datReq == "CT1") {                                //Do the following if Temperature is requested   
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.println(Irms1); 
      Udp.endPacket();                                            //End the packet
    }   

    if (datReq == "CT2") {                                //Do the following if Temperature is requested      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(Irms2);  
      Udp.endPacket();                                            //End the packet
    } 

    if (datReq == "CT3") {                                //Do the following if Temperature is requested      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(Irms3); 
      Udp.endPacket();                                            //End the packet
    } 
    if (datReq == "CT4") {                                //Do the following if Temperature is requested      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(Irms4); 
      Udp.endPacket();                                            //End the packet
    } 

// ======================================================================================================
    if (datReq == "HotWater") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(HotWater); 
      Serial.println(HotWater);
      Udp.endPacket();                                            //End the packet
    }   

    if (datReq == "ColdWater") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(ColdWater); 
      Serial.println(ColdWater);
      Udp.endPacket();                                            //End the packet
    } 

    if (datReq == "DayElement") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(DayElement); 
      Serial.println(DayElement);
      Udp.endPacket();                                            //End the packet
    } 

    if (datReq == "NightElement") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(NightElement); 
      Serial.println(NightElement);
      Udp.endPacket();                                            //End the packet
    } 

// ======================================================================================================
    if (datReq == "HallwayLight") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(HallwayLight); 
      Serial.println(HallwayLight);
      Udp.endPacket();                                            //End the packet
    }   

// ======================================================================================================
    if (datReq == "LightsOn") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Lights On"); 
      Serial.println("Lights On");
      digitalWrite(lights, LOW);
      Udp.endPacket();                                            //End the packet
    } 
    
    if (datReq == "LightsOff") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Lights Off"); 
      Serial.println("Lights Off");
      digitalWrite(lights, HIGH);
      Udp.endPacket();                                            //End the packet
    } 

// ======================================================================================================
    if (datReq == "BulkheadLightsOn") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Bulkhead Lights On"); 
      Serial.println("Bulkhead Lights On");
      digitalWrite(bulkhead_lights, LOW);
      Udp.endPacket();                                            //End the packet
    } 
    
    if (datReq == "BulkheadLightsOff") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Bulkhead Lights Off"); 
      Serial.println("Bulkhead Lights Off");
      digitalWrite(bulkhead_lights, HIGH);
      Udp.endPacket();                                            //End the packet
    }   

// ======================================================================================================
    if (datReq == "InternalLightsOn") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Internal Lights On"); 
      Serial.println("Internal Lights On");
      digitalWrite(internal_lights, HIGH);
      Udp.endPacket();                                            //End the packet
    } 
    
    if (datReq == "InternalLightsOff") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Internal Lights Off"); 
      Serial.println("Internal Lights Off");
      digitalWrite(internal_lights, LOW);
      Udp.endPacket();                                            //End the packet
    } 

// ======================================================================================================      
  
    if (datReq == "Temperature") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      float t = dht.readTemperature();                            // Read the temperature sensor
      Udp.print(t);                                               // Send the temperature measurement out
      Serial.print("Temperature: ");                              // Print the temperature to the terminal
      Serial.print(t);
      Serial.println(" *C ");
      Udp.endPacket();                                            //End the packet
    } 

    if (datReq == "Humidity") {                                   //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      float h = dht.readHumidity();                               // Read the temperature sensor
      Udp.print(h);                                               // Send the temperature measurement out
      Serial.print("Humidity: ");                                 // Print the temperature to the terminal
      Serial.print(h);
      Serial.println(" % ");
      Udp.endPacket();                                            //End the packet
 }

memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE);                //clear out the packetBuffer array

delay(100);

/*
Serial.println("=== Water ===");
Serial.print("Hot water temperature: ");
Serial.println(HotWater);
Serial.print("Cold water temperature: ");
Serial.println(ColdWater);
Serial.print("Day element temperature: ");
Serial.println(DayElement);
Serial.print("Night element temperature: ");
Serial.println(NightElement);

Serial.println("=== Power usage ===");
Serial.print("CT1: ");
Serial.println(Irms1);
Serial.print("CT2: ");
Serial.println(Irms2);
Serial.print("CT3: ");
Serial.println(Irms3);
Serial.print("CT4: ");
Serial.println(Irms4);

Serial.println("=== Hallway ===");
Serial.print("Hallway motion 1: ");
Serial.println(HallMotion1);
Serial.print("Hallway motion 2: ");
Serial.println(HallMotion2);
Serial.print("Hallway Light: ");
Serial.println(HallwayLight);

//   testing the relays
digitalWrite(lights, LOW);
delay(500);
digitalWrite(lights, HIGH);
delay(500);
digitalWrite(bulkhead_lights, LOW);
delay(500);
digitalWrite(bulkhead_lights, HIGH);
delay(500);
digitalWrite(internal_lights, LOW);
delay(500);
digitalWrite(internal_lights, HIGH);
delay(500);
*/

}

}

