#!/usr/bin/env python3

from socket import *
import time

class jarvis_control_2(object):

# Door

# Hallway
	def hallway_light_on(self):
		address = ( '192.168.1.210', 5000) #define server IP and port
		client_socket = socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "LightsOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request
		#r_server.set("BathroomLightCommanded","on")
		print "turn on"

	def hallway_light_off(self):
		address = ( '192.168.1.210', 5000) #define server IP and port
		client_socket = socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "LightsOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request		
		#r_server.set("BathroomLightCommanded","off")
		print "turn off"

	def bulkhead_light_on(self):
		address= ( '192.168.1.210', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "BulkheadLightsOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request
		#r_server.set("BathroomLightCommanded","on")

	def bulkhead_light_off(self):
		address= ( '192.168.1.210', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "BulkheadLightsOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request		
		#r_server.set("BathroomLightCommanded","off")

	def internal_light_on(self):
		address= ( '192.168.1.210', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "InternalLightsOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request
		#r_server.set("BathroomLightCommanded","on")

	def internal_light_off(self):
		address= ( '192.168.1.210', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "InternalLightsOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request		
		#r_server.set("BathroomLightCommanded","off")

# Bathroom
	def bathroom_light_on(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "LightsOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request
		#r_server.set("BathroomLightCommanded","on")

	def bathroom_light_off(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "LightsOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request		
		#r_server.set("BathroomLightCommanded","off")

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
		address= ( '192.168.1.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "HackerspaceDeskOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	   

	def hackerspace_desk_off(self):
		address= ( '192.168.1.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "HackerspaceDeskOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	
	
	def hackerspace_lights_on(self):
		address= ( '192.168.1.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "Relay1On" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	    

	def hackerspace_lights_off(self):
		address= ( '192.168.1.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "Relay1Off" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	

# Loft
	def loft_fan_on(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "Relay3On" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def loft_fan_off(self):
		address= ( '192.168.1.235', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "Relay3Off" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	

# Bedroom
	def bedroom_lamp_on(self):
		address= ( '192.168.1.215', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "BedroomLampOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	    

	def bedroom_lamp_off(self):
		address= ( '192.168.1.215', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "BedroomLampOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	
	
	def bedroom_desk_on(self):
		address= ( '192.168.1.215', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "BedroomDeskOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	   

	def bedroom_desk_off(self):
		address= ( '192.168.1.215', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "BedroomDeskOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	

# Living Room
	def alexa_speaker_on(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "AlexaOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def alexa_speaker_off(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "AlexaOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def tv_on(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "TVOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request	    

	def tv_off(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "TVOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request 
	
	def living_room_lamp_on(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "MainLampOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request    

	def living_room_lamp_off(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "MainLampOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def living_room_chairlamp_on(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "ChairLampOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def living_room_chairlamp_off(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "ChairLampOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def pc_peripherals_on(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "PCperipheralsOn" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request 

	def pc_peripherals_off(self):
		address= ( '192.168.1.225', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "PCperipheralsOff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

# Kitchen
	def kitchen_lights_on(self):
		address= ( '192.168.68.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "5Von" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def kitchen_lights_off(self):
		address= ( '192.168.68.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "5Voff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

	def kitchen_underlights_on(self):
		address= ( '192.168.68.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "12Von" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request 

	def kitchen_underlights_off(self):
		address= ( '192.168.68.220', 5000) #define server IP and port
		client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
		client_socket.settimeout(1) #Only wait 1 second for a response
		data = "12Voff" #Set data request to Pressure
		client_socket.sendto( data, address) #Send the data request

# Water

# Power

"""
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
        #Read the switch state and return its current value.
        return GPIO.input(SWITCH_PIN)

    def set_led(self, value):
        #Set the LED to the provided value (True = on, False = off).
        GPIO.output(LED_PIN, value)

    def return_test(self):
    	return 'hello world'		
"""