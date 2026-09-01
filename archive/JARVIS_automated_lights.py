#!/usr/bin/env python3

from socket import *
import datetime
import time
import ephem

import jarvis_control_2

"""
print ("Current Year is: %d" % currentDT.year)
print ("Current Month is: %d" % currentDT.month)
print ("Current Day is: %d" % currentDT.day)
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)
print ("Current Microsecond is: %d" % currentDT.microsecond)
"""

o=ephem.Observer()  
o.lat='51.3168'  
o.long='0.56'  
s=ephem.Sun()  
s.compute()  

time_state = "unknown"
light_state = "unknown"

while True:

    time.sleep(10)

    sun_rise = ephem.localtime(o.next_rising(s))
    noon = ephem.localtime(o.next_transit(s))
    sun_set = ephem.localtime(o.next_setting(s))
    currentDT = datetime.datetime.now()
    current_time = ("%s:%s" % (currentDT.hour, currentDT.minute))
    #current_time = "23:01"

    sun_set = str(sun_set)
    sun_set = sun_set[11:16]

    sun_rise = str(sun_rise)
    sun_rise = sun_rise[11:16]

    #print sun_rise
    #print noon
    #print sun_set
    #print current_time

# day
    if current_time > sun_rise and current_time < sun_set:
        print "it's after sun rise and before sun_set - Day"
        if time_state != "day":
            time_state = "day"
            light_state = "off"
            print time_state
            print light_state

# evening
    if current_time > sun_set and current_time < "23:00":
        print "it's after sun_set and before 11pm - evening"
        if time_state != "evening":
            time_state = "evening"
            light_state = "on"
            print time_state
            print light_state   

# night
    if current_time > "23:00" and current_time > sun_rise:
        print "it's after 11pm and before sun rise - night"
        if time_state != "night":
            time_state = "night"
            light_state = "night"
            print time_state
            print light_state

    if light_state == "off":
        print "turning lights off"
    # chair lamp    
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "ChairLampOff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # bulkhead lights
        address= ( '192.168.1.210', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "BulkheadLightsOff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # kitchen lights
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "5Voff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # living room light
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "MainLampOff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request    
    elif light_state == "on":
        print "turning lights on"
    # chair lamp    
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "ChairLampOn" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # bulkhead lights
        address= ( '192.168.1.210', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "BulkheadLightsOn" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # kitchen lights
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "5Von" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # living room light
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "MainLampOn" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request   
    elif light_state == "night":
        print "night lights on"
    # chair lamp    
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "ChairLampOff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # bulkhead lights
        address= ( '192.168.1.210', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "BulkheadLightsOn" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # kitchen lights
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "5Voff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
    # living room light
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "MainLampOff" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request  