""" fauxmo_minimal.py - Fabricate.IO

    This is a demo python file showing what can be done with the debounce_handler.
    The handler prints True when you say "Alexa, device on" and False when you say
    "Alexa, device off".

    If you have two or more Echos, it only handles the one that hears you more clearly.
    You can have an Echo per room and not worry about your handlers triggering for
    those other rooms.

    The IP of the triggering Echo is also passed into the act() function, so you can
    do different things based on which Echo triggered the handler.
"""

import fauxmo
import logging
import time

import SocketServer

from debounce_handler import debounce_handler

from thing import PiThing
from jarvis_control import jarvis_control

logging.basicConfig(level=logging.DEBUG)

jarvis_control = jarvis_control()
pi_thing = PiThing()

class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """

    # add new devices here
    TRIGGERS = {
    # Door
        # nothing to activate
    # Hallway
        "hallway": 52001,
        "bulkhead": 52002,
    # Bathroom
        "bathroom": 52003,
    # Hackerspace
        "hackerspace": 52004,
        "hackerspace desk": 52005,        
    # Loft
        "server": 52006,
    # Bedroom
        "bedroom": 52007,
    # Living Room
        "chair lamp": 52008,
        "speaker": 52009,
        "lamp": 52010,
        "light": 52011,
        "television": 52012,
        "computer": 52013,                                
    # Kitchen
        "kitchen": 52014
    # Water
        # nothing to activate
    # Power
        # nothing to activate
    # Debug 
        # nothing to activate
    }

    def act(self, client_address, state, name):
    # Door

    # Hallway
        if name == 'hallway':
            if state == True:
                pi_thing.set_hallway(0)
                print "hallway light is on"
            elif state == False:
                pi_thing.set_hallway(1)
                print "hallway light is off"

        if name == 'bulkhead':
            if state == True:
                pi_thing.set_bulkhead(0)
                print "bulkhead light is on"
            elif state == False:
                pi_thing.set_bulkhead(1)
                print "bulkhead light is off"

    # Bathroom
        if name == 'bathroom':
            if state == True:
                jarvis_control.bathroom_light_on()
                print "bathroom light is on"
            elif state == False:
                jarvis_control.bathroom_light_off()
                print "bathroom light is off"

    # Hackerspace
        if name == 'hackerspace':
            if state == True:
                jarvis_control.hackerspace_lights_on()
                print "hackerspace light is on"
            elif state == False:
                jarvis_control.hackerspace_lights_off()
                print "hackerspace light is off"

        if name == 'hackerspace desk':
            if state == True:
                jarvis_control.hackerspace_desk_on()
                print "hackerspace desk is on"
            elif state == False:
                jarvis_control.hackerspace_desk_off()
                print "hackerspace desk is off"

    # Loft
        if name == 'server':
            print "turning the server on"

    # Bedroom
        if name == 'bedroom':
            if state == True:
                jarvis_control.bedroom_lamp_on()
                print "bedroom light is on"
            elif state == False:
                jarvis_control.bedroom_lamp_off()
                print "bedroom light is off"

    # Living Room  
        if name == 'speaker':
            if state == True:
                jarvis_control.alexa_speaker_on()
                print "alexa speaker is on"
            elif state == False:
                jarvis_control.alexa_speaker_off()
                print "alexa speaker is off"

        if name == 'television':
            if state == True:
                jarvis_control.tv_on()
                print "television is on"
            elif state == False:
                jarvis_control.tv_off()
                print "television is off"

        if name == 'living room':
            if state == True:
                jarvis_control.living_room_chairlamp_on()
                print "chair lamp light is on"
            elif state == False:
                jarvis_control.living_room_chairlamp_on()
                print "chair lamp light is off"

        if name == 'computer':
            if state == True:
                jarvis_control.pc_peripherals_on()
                print "pc peripherals are on"
            elif state == False:
                jarvis_control.pc_peripherals_off()
                print "pc peripherals are off"
   
    # Kitchen
        if name == 'kitchen':
            if state == True:
                jarvis_control.kitchen_light_on()
                print "kitchen light is on"
            elif state == False:
                jarvis_control.kitchen_light_off()
                print "kitchen light is off"  

    # Water

    # Power

    # Debug 

        return True

if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
            break
