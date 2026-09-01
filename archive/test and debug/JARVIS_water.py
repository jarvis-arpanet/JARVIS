#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address =  ( '192.168.1.210', 5000) #define server IP and port

client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= Hot Water Pipe =========================

    data = "HotWater" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Hot water temperature is ", temp, " degrees C." # print the result
        water_hot = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Cold Water Pipe =========================

    data = "ColdWater" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Cold water temperature is ", temp, " degrees C." # print the result
        water_cold = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Daytime Water Element =========================

    data = "DayElement" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Day element Temperature is ", temp, " degrees C." # print the result
        water_day = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Nighttime Water Element =========================

    data = "NightElement" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Econ7 Temperature is ", temp, " degrees C." # print the result
        water_night = temp
    except:
        pass
    time.sleep(1) #delay before sending next command
    
# ========================= end =========================
