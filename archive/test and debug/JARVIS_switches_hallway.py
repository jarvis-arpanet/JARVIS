#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address =  ( '192.168.1.210', 5000) #define server IP and port

client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= Bulkhead Lights =========================
    data = "BulkheadLightsOn" #Set data request to Pressure
 
    client_socket.sendto( data, address) #Send the data request
 
    try:
 
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Bulkhead light On" # Print the result
 
    except:
        pass
 
    time.sleep(1) #delay before sending next command

    data = "BulkheadLightsOff" #Set data request to Pressure
 
    client_socket.sendto( data, address) #Send the data request
 
    try:
 
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Bulkhead light Off" # Print the result
 
    except:
        pass
 
    time.sleep(1) #delay before sending next command

# ========================= Internal Light =========================
    data = "InternalLightsOn" #Set data request to Pressure
 
    client_socket.sendto( data, address) #Send the data request
 
    try:
 
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Internal light On" # Print the result
 
    except:
        pass
 
    time.sleep(1) #delay before sending next command

    data = "InternalLightsOff" #Set data request to Pressure
 
    client_socket.sendto( data, address) #Send the data request
 
    try:
 
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Internal light Off" # Print the result
 
    except:
        pass
 
    time.sleep(1) #delay before sending next command

# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(1) # only check every minute
