#!/usr/bin/env python3

from socket import *
import time
import csv # this is to write the results to a comma seperated value file
 
address = ( '192.168.1.235', 5000) #define server IP and port
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

while(1):

# ========================= Loft Light =========================

    data = "LoftLight" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Loft Light is ", temp # Print the result
        with open('record_JARVIS.csv', 'a') as record:
            write_date = time.strftime('%Y-%m-%d') # these are seperated because Py did not like comma between time and date
            write_time = time.strftime('%H:%M')
            writer = csv.writer(record)
            writer.writerow([write_date,write_time,"Loft light",rec_data]) 
        record.close ()
    except:
        pass
    time.sleep(0.1) #delay before sending next command

# ========================= Hallway Light =========================

    data = "HallwayLight" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Hallway Light is ", temp # Print the result
        with open('record_JARVIS.csv', 'a') as record:
            write_date = time.strftime('%Y-%m-%d') # these are seperated because Py did not like comma between time and date
            write_time = time.strftime('%H:%M')
            writer = csv.writer(record)
            writer.writerow([write_date,write_time,"Hallway light",rec_data]) 
        record.close ()
    except:
        pass
    time.sleep(0.1) #delay before sending next command    

# ========================= Hallway Light =========================

    data = "BathroomLight" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The Bathroom Light is ", temp # Print the result
        with open('record_JARVIS.csv', 'a') as record:
            write_date = time.strftime('%Y-%m-%d') # these are seperated because Py did not like comma between time and date
            write_time = time.strftime('%H:%M')
            writer = csv.writer(record)
            writer.writerow([write_date,write_time,"Bathroom light",rec_data]) 
        record.close ()
    except:
        pass
    time.sleep(0.1) #delay before sending next command    

# ========================= Bathroom Temperature =========================

    data = "Temperature" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The temperature is ", temp, "*C" # Print the result

    except:
        pass
    time.sleep(0.1) #delay before sending next command    


# ========================= Bathroom Humidity =========================

    data = "Humidity" #Set data request to Temperature
    client_socket.sendto( data, address) #Send the data request
 
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        temp = float(rec_data) #Convert string rec_data to float temp
        print "The humidity is ", temp,"%" # Print the result

    except:
        pass
    time.sleep(0.1) #delay before sending next command    



# ========================== Shower Lights ========================

    data = "LightsOn" #Set data request to Pressure
 
    client_socket.sendto( data, address) #Send the data request
 
    try:
 
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Lights On" # Print the result
 
    except:
        pass
 
    time.sleep(1) #delay before sending next command


# ========================== Extractor Fan ========================

    data = "FanOn" #Set data request to Pressure
 
    client_socket.sendto( data, address) #Send the data request
 
    try:
 
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        #Pressure = float(rec_data) #Convert string rec_data to float temp
        print "Fan On" # Print the result
 
    except:
        pass
 
    time.sleep(1) #delay before sending next command



# ========================= end =========================
    print "" # leave a space before starting to read all the data again
    time.sleep(0.1) # only check every minute

