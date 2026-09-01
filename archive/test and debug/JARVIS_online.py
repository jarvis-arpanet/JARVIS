#!/usr/bin/env python3

"""
1	192.168.0.27	DESKTOP-O3EMKI3	ac:72:89:dc:be:32
2	192.168.0.6	    WilliamsiPhone3	b0:9f:ba:ce:e3:ea
3	192.168.0.240	UNKNOWN	de:ad:be:ef:fe:ee
4	192.168.0.10	HP44291F	d0:bf:9c:44:29:1f
5	192.168.0.40	jarvis-door	48:02:2a:1b:76:33
6	192.168.0.34	JARVIS_HUB	b8:27:eb:84:39:c1
7	192.168.0.26	Lauras-iPhone	44:00:10:21:fe:65
8	192.168.0.17	UNKNOWN	d8:cb:8a:9c:09:2c
9	192.168.0.33	JARVIS_HUB	b8:27:eb:d1:6c:94
"""

import pyping
import time
import csv

while(1):
# Google
    r = pyping.ping('google.com')
    if r.ret_code == 0:
        print("Google is up")
        google = 'up'
    else:
        print("Google is down")
        google = 'down'
# Desktop
    r = pyping.ping('192.168.1.65')
    if r.ret_code == 0:
        print("Desktop is up")
        desktop = 'up'
    else:
        print("Desktop is down")
        desktop = 'down'
# iPhone
    r = pyping.ping('192.168.1.83')
    if r.ret_code == 0:
        print("iPhone is up")
        iphone = 'up'
    else:
        print("iPhone is down")
        iphone = 'down'
# JARVIS Cupboard
    r = pyping.ping('192.168.1.6')
    if r.ret_code == 0:
        print("Cupboard is up")
        cupboard = 'up'
    else:
        print("Cupboard is down")
        cupboard = 'down'
# JARVIS Door
    r = pyping.ping('192.168.1.66')
    if r.ret_code == 0:
        print("Door is up")
        door = 'up'
    else:
        print("Door is down")
        door = 'down'
# JARVIS Server
    r = pyping.ping('192.168.1.80')
    if r.ret_code == 0:
        print("Server is up")
        server = 'up'
    else:
        print("Server is down")
        server = 'down'

"""
with open('JARVIS_online.csv', 'a') as record:
    write_date = time.strftime('%Y-%m-%d') # these are seperated because Py did not like comma between time and date
    write_time = time.strftime('%H:%M')
    writer = csv.writer(record)
    writer.writerow([google,desktop,iphone,cupboard,door,server]) 
record.close () 
"""
