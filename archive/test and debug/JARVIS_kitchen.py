#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address = ( '192.168.1.225', 5000) #define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

    data = "5Von" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "5V On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "5Voff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "5V Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "12Von" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "12V On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "12Voff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "12V Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command


    data = "ChairLampOn" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Chair Lamp On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "ChairLampOff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Chair Lamp Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command


# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(0.1) # only check every minute
