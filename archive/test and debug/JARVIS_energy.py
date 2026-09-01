#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file

address_energymonitor = ( '192.168.1.210', 5000)

client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= CT1 =========================
    client_socket.sendto( "CT1", address_energymonitor) #Send the data request
    try:
        CT1, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT1 = float(CT1) #Convert string rec_data to float temp
        print "CT1 is:", CT1, " Amps rms." # print the result
    except:
        print("error on CT1")
    time.sleep(0.5) #delay before sending next command
# ========================= CT2 =========================
    client_socket.sendto( "CT2", address_energymonitor) #Send the data request
    try:
        CT2, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT2 = float(CT2) #Convert string rec_data to float temp
        print "CT2 is:", CT2, " Amps rms." # print the result
    except:
        print("error on CT2")
    time.sleep(0.5) #delay before sending next command
# ========================= CT3 =========================
    client_socket.sendto( "CT3", address_energymonitor) #Send the data request
    try:
        CT3, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT3 = float(CT3) #Convert string rec_data to float temp
        print "CT3 is:", CT3, " Amps rms." # print the result
    except:
        print("error on CT3")
    time.sleep(0.5) #delay before sending next command 
# ========================= CT4 =========================
    client_socket.sendto( "CT4", address_energymonitor) #Send the data request
    try:
        CT4, addr = client_socket.recvfrom(2048) #Read response from arduino
        CT4 = float(CT4) #Convert string rec_data to float temp
        print "CT4 is:", CT4, " Amps rms." # print the result
    except:
        print("error on CT4")
    time.sleep(0.5) #delay before sending next command     

# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(1) # only check every minute
