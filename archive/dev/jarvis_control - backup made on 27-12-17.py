#!/usr/bin/env python3

from socket import *
import time
import csv
import pi_switch
import redis
import RPi.GPIO as GPIO

LED_PIN     = 22
bulkhead_light = 15
hallway_light  = 14
SWITCH_PIN    = 24

r_server = redis.Redis("localhost")

class jarvis_control(object):

    def __init__(self):
        """Initialize the 'thing'."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(bulkhead_light, GPIO.OUT)
        GPIO.setup(hallway_light, GPIO.OUT)
        GPIO.setup(SWITCH_PIN, GPIO.IN)

# Door

# Hallway
	def set_bulkhead(self, value):
		GPIO.output(bulkhead_light, value)

	def set_hallway(self, value):
		GPIO.output(hallway_light, value)

# Bathroom
	def bathroom_light_on(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "LightsOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request
		r_server.set("BathroomLightCommanded","on")

	def bathroom_light_off(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "LightsOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request		
		r_server.set("BathroomLightCommanded","off")

	def bathroom_fan_on(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "FanOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def bathroom_fan_off(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "FanOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	

# Hackerspace
	def hackerspace_desk_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1381717, 24) # switch on	    

	def hackerspace_desk_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1381716, 24) # switch on
	
	def hackerspace_lights_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(5510485, 24) # switch on	    

	def hackerspace_lights_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(5510484, 24) # switch on

# Loft

# Bedroom
	def bedroom_lamp_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(5313877, 24) # switch on	    

	def bedroom_lamp_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(5313876, 24) # switch on
	
	def bedroom_hair_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(5326165, 24) # switch on	    

	def bedroom_hair_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(5326164, 24) # switch on

# Living Room
	def alexa_speaker_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(4527445, 24) # switch on	    

	def alexa_speaker_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(4527444, 24) # switch on	

	def tv_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1381717, 24) # switch on	    

	def tv_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1381716, 24) # switch on	 
	
	def living_room_lamp_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1397845, 24) # switch on	    

	def living_room_lamp_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1397844, 24) # switch on	

	def living_room_chairlamp_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1394005, 24) # switch on	    

	def living_room_chairlamp_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1394004, 24) # switch on	
	
	def pc_peripherals_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1397077, 24) # switch on	    

	def pc_peripherals_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(1397076, 24) # switch on	

# Kitchen

# Water

# Power

# Debug
	def test_switch_on(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(4527445, 24) # switch on	    

	def test_switch_off(self):
		sender = pi_switch.RCSwitchSender()
		sender.enableTransmit(0) # use WiringPi pin 0
		sender.sendDecimal(4527444, 24) # switch on	 

    def read_switch(self):
        """Read the switch state and return its current value.
        """
        return GPIO.input(SWITCH_PIN)

    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off).
        """
        GPIO.output(LED_PIN, value)		