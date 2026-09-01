/*
  JARVIS_bathroom

  Purpose: the bathroom node of the JARVIS home automation system, also includes the loft
  Modified: 08/01/2017
*/

#include "DHT.h"
#define DHTPIN 2     // what digital pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

#include <Ethernet.h>                                            //Load Ethernet Library
#include <EthernetUdp.h>                                         //Load the Udp Library
#include <SPI.h>                                                 //Load SPI Library
//#include "Wire.h"                                                //imports the wire library
//#include <math.h>                                                //imports the math library for the temperature calc.
 
float tempC;                                                     //Declare variable for Temp in C

byte mac[] ={ 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEF};               //Assign mac address
IPAddress ip(192, 168, 1, 235);                                  //Assign the IP Adress
unsigned int localPort = 5000;                                   //Assign a port to talk over
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];                       //dimensian a char array to hold our data packet
String datReq;                                                   //String for our data
int packetSize;                                                  //Size of the packet
EthernetUDP Udp;                                                 //Create a UDP Object

int lights = 9;
int fan = 8;
int relay3 = 11;
int relay4 = 12;

const int analogInPin0 = A2;                                      // Analog input pin that the potentiometer is attached to
const int analogInPin1 = A3;                                      // Analog input pin that the potentiometer is attached to
const int analogInPin2 = A4;                                      // Analog input pin that the potentiometer is attached to

int A0_Value = 0;        // value read from the pot
int A1_Value = 0;        // value read from the pot
int A2_Value = 0;        // value read from the pot

int LoftLight = 0;
int HallwayLight = 0;
int BathroomLight = 0;

void setup() {
  
  Serial.begin(9600);                                             //Initialize Serial Port 
  Ethernet.begin( mac, ip);                                       //Inialize the Ethernet
  Udp.begin(localPort);                                           //Initialize Udp
  delay(1500);                                                    //delay

  pinMode(fan, OUTPUT);
  pinMode(lights, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);

  digitalWrite(fan, HIGH);
  digitalWrite(lights, HIGH);
  digitalWrite(relay3, HIGH);
  digitalWrite(relay4, HIGH);
  
  dht.begin();
}

void loop() {
  
  packetSize =Udp.parsePacket();                                  //Reads the packet size
  
  LoftLight = analogRead(analogInPin0);
  HallwayLight = analogRead(analogInPin2);
  BathroomLight = analogRead(analogInPin1);

  if(packetSize>0) {                                              //if packetSize is >0, that means someone has sent a request
    
  Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);               //Read the data request
  String datReq(packetBuffer);                                  //Convert char array packetBuffer into a string called datReq

// ======================================================================================================




// ================================= Light sensors ======================================================
    
    if (datReq == "LoftLight") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(LoftLight); 
      Serial.println(LoftLight);
      Udp.endPacket();                                            //End the packet
    } 

    if (datReq == "HallwayLight") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(HallwayLight); 
      Serial.println(HallwayLight);
      Udp.endPacket();                                            //End the packet
    } 

    if (datReq == "BathroomLight") {                                //Do the following if Temperature is requested
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print(BathroomLight); 
      Serial.println(BathroomLight);
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
    if (datReq == "FanOn") {                                //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Fan On"); 
      Serial.println("Fan On");
      digitalWrite(fan, LOW);      
      Udp.endPacket();                                            //End the packet
    } 
    
    if (datReq == "FanOff") {                                //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Fan Off"); 
      Serial.println("Fan Off");
      digitalWrite(fan, HIGH);
      Udp.endPacket();                                            //End the packet
    }     

// ======================================================================================================
    if (datReq == "Relay3On") {                                //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Fan On"); 
      Serial.println("Fan On");
      digitalWrite(relay3, LOW);      
      Udp.endPacket();                                            //End the packet
    } 
    
    if (datReq == "Relay3Off") {                                //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Fan Off"); 
      Serial.println("Fan Off");
      digitalWrite(relay3, HIGH);
      Udp.endPacket();                                            //End the packet
    }  

// ======================================================================================================
    if (datReq == "Relay4On") {                                //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Fan On"); 
      Serial.println("Fan On");
      digitalWrite(relay4, LOW);      
      Udp.endPacket();                                            //End the packet
    } 
    
    if (datReq == "Relay4Off") {                                //Do the following if Temperature is requested      
      
      Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());          //Initialize packet send
      Udp.print("Fan Off"); 
      Serial.println("Fan Off");
      digitalWrite(relay4, HIGH);
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
  
  }
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE);                //clear out the packetBuffer array
}
