#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address = ( '192.168.1.220', 5000) #define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= Hackspace Light =========================
    client_socket.sendto( "HackerspaceLight", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Hackerspace Light is ", temp # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Motion =========================
    client_socket.sendto( "HackerspaceMotion", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Hackerspace Motion is ", temp # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Temperature =========================
    client_socket.sendto( "HackerspaceTemperature", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Hackerspace Temperature is ", temp, " C" # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Humidity =========================
    client_socket.sendto( "HackerspaceHumidity", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "Hackerspace Humidity is ", temp, " %" # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Relay 1 =========================
    data = "Relay1On" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Relay 1 On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "Relay1Off" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Relay 1 Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Relay 2 =========================
    data = "Relay2On" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Relay 2 On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "Relay2Off" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Relay 2 Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Desk =========================
    data = "HackerspaceDeskOn" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Hackerspace Desk On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "HackerspaceDeskOff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Hackerspace Desk Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(0.1) # only check every minute
