#! /usr/bin/env python

# Type B example: address group = 1, channel = 1
import pi_switch
import time

sender = pi_switch.RCSwitchSender()

while True:
	sender.enableTransmit(0) # use WiringPi pin 0
	sender.sendDecimal(4527445, 24) # switch on
	time.sleep(5)
	sender.enableTransmit(0) # use WiringPi pin 0
	sender.sendDecimal(4527444, 24) # switch on
	time.sleep(5)