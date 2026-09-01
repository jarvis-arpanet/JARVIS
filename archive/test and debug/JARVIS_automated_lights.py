#!/usr/bin/env python3

from socket import *
import datetime
import time

"""
print ("Current Year is: %d" % currentDT.year)
print ("Current Month is: %d" % currentDT.month)
print ("Current Day is: %d" % currentDT.day)
print ("Current Hour is: %d" % currentDT.hour)
print ("Current Minute is: %d" % currentDT.minute)
print ("Current Second is: %d" % currentDT.second)
print ("Current Microsecond is: %d" % currentDT.microsecond)
"""

while True:

    currentDT = datetime.datetime.now()

    if currentDT.minute == 6:
        address= ( '192.168.1.225', 5000) #define server IP and port
        client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
        client_socket.settimeout(1) #Only wait 1 second for a response
        data = "ChairLampOn" #Set data request to Pressure
        client_socket.sendto( data, address) #Send the data request
        print "light on"
    else:
        print ("Current Minute is: %d" % currentDT.minute)

    time.sleep(10)