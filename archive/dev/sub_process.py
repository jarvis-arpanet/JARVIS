#!/usr/bin/env python3

from socket import *
import time

class sub_process(object):

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