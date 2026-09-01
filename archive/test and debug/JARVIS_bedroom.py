#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address = ( '192.168.1.215', 5000) #define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= Bedroom Light =========================
    client_socket.sendto( "BedroomLight", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Light is ", temp # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Bedroom Temperature =========================
    client_socket.sendto( "BedroomTemperature", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Temperature is ", temp, " C" # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Bedroom Humidity =========================
    client_socket.sendto( "BedroomHumidity", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Humidity is ", temp, " %" # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Bedroom Desk =========================
    data = "BedroomDeskOn" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Desk On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "BedroomDeskOff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Desk Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Bedroom Lamp =========================
    data = "BedroomLampOn" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Lamp On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "BedroomLampOff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Bedroom Lamp Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(0.1) # only check every minute
