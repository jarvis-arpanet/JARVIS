#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address = ( '192.168.68.220', 5000) #define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):
# ========================= Kitchen Light =========================

    data = "KitchenLight" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Kitchen Light is ", temp # Print the result
    except:
        pass
    time.sleep(0.1) #delay before sending next command

# ========================= Kitchen Motion =========================

    data = "KitchenMotion" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Kitchen Motion is ", temp # Print the result
    except:
        pass
    time.sleep(0.1) #delay before sending next command

# ========================= Kitchen Temperature =========================

    data = "KitchenTemperature" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The temperature is ", temp, "*C" # Print the result

    except:
        pass
    time.sleep(0.1) #delay before sending next command    

# ========================= Kitchen Humidity =========================

    data = "KitchenHumidity" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The humidity is ", temp,"%" # Print the result

    except:
        pass
    time.sleep(0.1) #delay before sending next command    

# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(1) # only check every minute
