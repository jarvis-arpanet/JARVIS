#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address =  ( '192.168.1.210', 5000) #define server IP and port

client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= Hot Water Pipe =========================
    client_socket.sendto( "HotWater", address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Hot water temperature is ", temp, " degrees C." # print the result
        water_hot = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Cold Water Pipe =========================
    client_socket.sendto( "ColdWater", address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Cold water temperature is ", temp, " degrees C." # print the result
        water_cold = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Daytime Water Element =========================
    client_socket.sendto( "DayElement", address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Day element Temperature is ", temp, " degrees C." # print the result
        water_day = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Nighttime Water Element =========================
    client_socket.sendto( "NightElement", address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Econ7 Temperature is ", temp, " degrees C." # print the result
        water_night = temp
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= CT1 =========================
    client_socket.sendto( "CT1", address) #Send the data request
    try:
        CT1, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT1 = float(CT1) #Convert string rec_data to float temp
        print "CT1 is:", CT1, " Amps rms." # print the result
    except:
        print("error on CT1")
    time.sleep(1) #delay before sending next command

# ========================= CT2 =========================
    client_socket.sendto( "CT2", address) #Send the data request
    try:
        CT2, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT2 = float(CT2) #Convert string rec_data to float temp
        print "CT2 is:", CT2, " Amps rms." # print the result
    except:
        print("error on CT2")
    time.sleep(1) #delay before sending next command

# ========================= CT3 =========================
    client_socket.sendto( "CT3", address) #Send the data request
    try:
        CT3, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT3 = float(CT3) #Convert string rec_data to float temp
        print "CT3 is:", CT3, " Amps rms." # print the result
    except:
        print("error on CT3")
    time.sleep(1) #delay before sending next command 

# ========================= CT4 =========================
    client_socket.sendto( "CT4", address) #Send the data request
    try:
        CT4, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT4 = float(CT4) #Convert string rec_data to float temp
        print "CT4 is:", CT4, " Amps rms." # print the result
    except:
        print("error on CT4")
    time.sleep(1) #delay before sending next command    

# ========================= Temperature =========================
    client_socket.sendto( "Temperature", address) #Send the data request
    try:
        Temperature, addr = client_socket.recvfrom(2048) #Read response from arduino
        Temperature = float(Temperature) #Convert string rec_data to float temp
        print "The temperature is ", Temperature, "*C" # Print the result
    except:
        pass
    time.sleep(0.1) #delay before sending next command    

# ========================= Humidity =========================
    client_socket.sendto( "Humidity", address) #Send the data request
    try:
        Humidity, addr = client_socket.recvfrom(2048) #Read response from arduino
        Humidity = float(Humidity) #Convert string rec_data to float temp
        print "The humidity is ", Humidity,"%" # Print the result
    except:
        pass
    time.sleep(0.1) #delay before sending next command    

"""

# ========================== Kitchen Lights ========================
    data = "LightsOn" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Lights On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "UnderLightsOn" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Under lights On" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command
"""
"""

    data = "LightsOff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Lights Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

    data = "UnderLightsOff" #Set data request to Pressure
    client_socket.sendto( data, address) #Send the data request
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Under lights  Off" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    

"""  
