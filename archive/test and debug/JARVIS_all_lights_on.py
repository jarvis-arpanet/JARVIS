import RPi.GPIO as GPIO ## Import GPIO library
import time
import subprocess                                                   # used for wakeonlan
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use BCM pin numbering ***IMPORTANT***

# =========================== GPIO IN =========================== 
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)                  # MUX IN - SIG
GPIO.setup(6, GPIO.OUT)                                             # MUX IN - S3
GPIO.setup(13, GPIO.OUT)                                            # MUX IN - S2
GPIO.setup(19, GPIO.OUT)                                            # MUX IN - S1
GPIO.setup(26, GPIO.OUT)                                            # MUX IN - S0

# =========================== GPIO OUT =========================== 
GPIO.setup(22, GPIO.OUT)                                            # DEBUG LED
GPIO.setup(14, GPIO.OUT)                                            # Hallway Light - Main
GPIO.setup(15, GPIO.OUT)                                            # Hallway Light - Bulkhead
GPIO.setup(18, GPIO.OUT)                                            # Internal HUB light
                                                                    # GPIO 17 - 433 Tx
                                                                    # GPIO 23 - 433 Rx

GPIO.setup(27, GPIO.OUT)                                            # MUX OUT  - ENABLE
GPIO.setup(21, GPIO.OUT)                                            # MUX OUT  - S0
GPIO.setup(20, GPIO.OUT)                                            # MUX OUT  - S1
GPIO.setup(16, GPIO.OUT)                                            # MUX OUT  - S2
GPIO.setup(12, GPIO.OUT)                                            # MUX OUT  - S3

# =========================== Set variables =========================== 
Blue1 = 0
Blue2 = 0
Blue3 = 0
Blue4 = 0
Blue5 = 0
Blue6 = 0
Blue7 = 0
Blue8 = 0
Blue9 = 0
Blue10 = 0

White1 = 0
White2 = 0
White3 = 0
White4 = 0
White5 = 0
White6 = 0

CurrentMinute = 0
LightOnTimer = None

switch10_state = 0

# =========================== Set Defaults =========================== 
GPIO.output(14, 1)
GPIO.output(15, 1)

# =========================== Main Loop =========================== 
while True:

    White4 = 1

# =========================== GPIO OUT - BUTTON FEEDBACK =========================== 
    OutputEnable = 1
    DEBUG = 0

    if OutputEnable == 1:
        GPIO.output(27,False) # True = OFF, enable
    else:
        GPIO.output(27,True)

    if DEBUG == 1:
        GPIO.output(22,True) # True = OFF, debug
    else:
        GPIO.output(22,False)

     # 0110 Blue 10
    if Blue10 == 1:
        GPIO.output(21,False)
        GPIO.output(20,True)
        GPIO.output(16,True)
        GPIO.output(12,False)
        time.sleep(0.001)
    
    # 1110 Blue 9
    if Blue9 == 1:
        GPIO.output(21,True)
        GPIO.output(20,True)
        GPIO.output(16,True)
        GPIO.output(12,False)
        time.sleep(0.001)

    # 0001 Blue 8
    if Blue8 == 1:
        GPIO.output(21,False)
        GPIO.output(20,False)
        GPIO.output(16,False)
        GPIO.output(12,True)
        time.sleep(0.001)

    # 0100 Blue 7
    if Blue7 == 1:
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,False)
        GPIO.output(12,True) 
        time.sleep(0.001)

    # 0101 Blue 6
    if Blue6 == 1:
        GPIO.output(21,False)
        GPIO.output(20,True)
        GPIO.output(16,False)
        GPIO.output(12,True) 
        time.sleep(0.001)

    # 1101 Blue 5
    if Blue5 == 1:
        GPIO.output(21,True)
        GPIO.output(20,True)
        GPIO.output(16,False)
        GPIO.output(12,True)
        time.sleep(0.001) 

    # 0011 Blue 4
    if Blue4 == 1:
        GPIO.output(21,False)
        GPIO.output(20,False)
        GPIO.output(16,True)
        GPIO.output(12,True)
        time.sleep(0.001)

    # 1011 Blue 3
    if Blue3 == 1:
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,True)
        GPIO.output(12,True) 
        time.sleep(0.001)  

    # 0111 Blue 2
    if Blue2 == 1:
        GPIO.output(21,False)
        GPIO.output(20,True)
        GPIO.output(16,True)
        GPIO.output(12,True) 
        time.sleep(0.001)

    # 1111 Blue 1
    if Blue1 == 1:
        GPIO.output(21,True)
        GPIO.output(20,True)
        GPIO.output(16,True)
        GPIO.output(12,True)
        time.sleep(0.001)

# =========================== GPIO OUT - Notifications =========================== 

    # 1001 White 6 checked
    if White6 == 1:
        GPIO.output(21,False)
        GPIO.output(20,False)
        GPIO.output(16,False)
        GPIO.output(12,False)
        time.sleep(0.001)

    # 1000 White 5 checked
    if White5 == 1:
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,False)
        GPIO.output(12,False) 
        time.sleep(0.001)

    # 0000 White 4?
    if White4 == 1:
        GPIO.output(21,False)
        GPIO.output(20,True)
        GPIO.output(16,False)
        GPIO.output(12,False) 
        time.sleep(0.001)

    # 1100 White 3
    if White3 == 1:
        GPIO.output(21,True)
        GPIO.output(20,True)
        GPIO.output(16,False)
        GPIO.output(12,False)
        time.sleep(0.001)
    
    # 0010 White 2
    if White2 == 1:
        GPIO.output(21,False)
        GPIO.output(20,False)
        GPIO.output(16,True)
        GPIO.output(12,False) 
        time.sleep(0.001)
    
    # 1010 White 1
    if White1 == 1:
        GPIO.output(21,True)
        GPIO.output(20,False)
        GPIO.output(16,True)
        GPIO.output(12,False) 
        time.sleep(0.001)

# Finish with GPIO clean-up    
GPIO.cleanup()
