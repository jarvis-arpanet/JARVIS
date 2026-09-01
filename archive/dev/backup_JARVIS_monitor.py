#!/usr/bin/env python3

# import the libraries
from socket import *
import time
import csv # this is to write the results to a comma seperated value file
import redis
from thing import PiThing
from jarvis_control import jarvis_control

# set the redis server and functions
r_server = redis.Redis("localhost")
pi_thing = PiThing()
jarvis_control = jarvis_control()

# set the IP addresses of the Arduinos
address_water = ( '192.168.1.240', 5000)
address_bathroom = ( '192.168.1.235', 5000)
address_energy = ( '192.168.1.230', 5000)

# setup the socket for the UDP packets
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response
 
def bathroom():
    print "=== Bathroom ==="
# ========================= Bathroom Temperature =========================
    client_socket.sendto( "Temperature", address_bathroom) #Send the data request
    try:
        global BathroomTemperature
        BathroomTemperature, addr = client_socket.recvfrom(2048) #Read response from arduino
        BathroomTemperature = float(BathroomTemperature) #Convert string rec_data to float temp
        print "The temperature is ", BathroomTemperature, "*C" # Print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command    
# ========================= Bathroom Humidity =========================
    client_socket.sendto( "Humidity", address_bathroom) #Send the data request
    try:
        global BathroomHumidity
        BathroomHumidity, addr = client_socket.recvfrom(2048) #Read response from arduino
        BathroomHumidity = float(BathroomHumidity) #Convert string rec_data to float temp
        print "The humidity is ", BathroomHumidity,"%" # Print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command    

    print "=== Loft ==="
# ========================= Loft Light =========================
    client_socket.sendto( "LoftLight", address_bathroom) #Send the data request
    try:
        global LoftLightReading
        LoftLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Loft Light is ", LoftLightReading # Print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command

    print "=== Hallway ==="
# ========================= Hallway Light =========================
    client_socket.sendto( "HallwayLight", address_bathroom) #Send the data request
    try:
        global HallwayLightReading
        HallwayLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Hallway Light is ", HallwayLightReading # Print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command    
# ========================= Hallway Light =========================
    client_socket.sendto( "BathroomLight", address_bathroom) #Send the data request
    try:
        global BathroomLightReading
        BathroomLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Bathroom Light is ", BathroomLightReading # Print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command 

def water():
    print "=== Water ==="
# ========================= Hot Water Pipe =========================
    client_socket.sendto( "HotWater", address_water) #Send the data request
    try:
        global HotWaterReading
        HotWaterReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Hot water temperature is ", HotWaterReading, " degrees C." # print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command
# ========================= Cold Water Pipe =========================
    client_socket.sendto( "ColdWater", address_water) #Send the data request
    try:
        global ColdWaterReading
        ColdWaterReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Cold water temperature is ", ColdWaterReading, " degrees C." # print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command
# ========================= Daytime Water Element =========================
    client_socket.sendto( "DayElement", address_water) #Send the data request
    try:
        global DayWaterElementReading
        DayWaterElementReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Day element Temperature is ", DayWaterElementReading, " degrees C." # print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command
# ========================= Nighttime Water Element =========================
    client_socket.sendto( "NightElement", address_water) #Send the data request
    try:
        global NightWaterElementReading
        NightWaterElementReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Econ7 Temperature is ", NightWaterElementReading, " degrees C." # print the result
    except:
        pass
    time.sleep(0.5) #delay before sending next command

def energy():
    print "=== Power ==="
# ========================= CT1 =========================
    client_socket.sendto( "CT1", address_energy) #Send the data request
    try:
        global Power_CT1
        Power_CT1, addr = client_socket.recvfrom(2048) #Read response from arduino
        Power_CT1 = float(Power_CT1) #Convert string rec_data to float temp
        Power_CT1 = Power_CT1/2
        print "CT1 - current consumption is", Power_CT1, " Amps rms." # print the result
        CT1_power = (Power_CT1*240)/1000
        CT1_cost = CT1_power*0.17
        CT1_cost = (round(CT1_cost,2))
        #print "Power consumpton is", CT1_power, "kWatts"
        #print "Power cost is ",CT1_cost
    except:
        Power_CT1 = ""
    time.sleep(0.5) #delay before sending next command
# ========================= CT2 =========================
    client_socket.sendto( "CT2", address_energy) #Send the data request
    try:
        global Power_CT2
        Power_CT2, addr = client_socket.recvfrom(2048) #Read response from arduino
        Power_CT2 = float(Power_CT2) #Convert string rec_data to float temp
        Power_CT2 = Power_CT2/2
        print "CT2 - current consumption is", Power_CT2, " Amps rms." # print the result
        CT2_power = (Power_CT2*240)/1000
        CT2_cost = CT2_power*0.17
        CT2_cost = (round(CT2_cost,2))
        #print "Power consumpton is", CT2_power, "kWatts"
        #print "Power cost is ",CT2_cost
    except:
        Power_CT2 = ""
    time.sleep(0.5) #delay before sending next command
# ========================= CT3 =========================
    client_socket.sendto( "CT3", address_energy) #Send the data request
    try:
        global Power_CT3
        Power_CT3, addr = client_socket.recvfrom(2048) #Read response from arduino
        Power_CT3 = float(Power_CT3) #Convert string rec_data to float temp
        Power_CT3 = Power_CT3/2
        print "CT3 - current consumption is", Power_CT3, " Amps rms." # print the result
        CT3_power = (Power_CT3*240)/1000
        CT3_cost = CT3_power*0.17
        CT3_cost = (round(CT3_cost,2))
        #print "Power consumpton is", CT3_power, "kWatts"
        #print "Power cost is ",CT3_cost
    except:
        Power_CT3 = ""
    time.sleep(0.5) #delay before sending next command    
# ========================= CT4 =========================
    client_socket.sendto( "CT4", address_energy) #Send the data request
    try:
        global Power_CT4
        Power_CT4, addr = client_socket.recvfrom(2048) #Read response from arduino
        Power_CT4 = float(Power_CT4) #Convert string rec_data to float temp
        Power_CT4 = Power_CT4/2
        print "CT4 - current consumption is", Power_CT4, " Amps rms." # print the result
        CT4_power = (Power_CT4*240)/1000
        CT4_cost = CT4_power*0.17
        CT4_cost = (round(CT4_cost,2))
        #print "Power consumpton is", CT4_power, "kWatts"
        #print "Power cost is ",CT4_cost
    except:
        Power_CT4 = ""
    time.sleep(0.5) #delay before sending next command

def redis_settings():
    print "=== Redis ==="    
# ========================= Redis =========================

# Door
    print "Door"
    r_server.set("Door Motion","-")
    r_server.set("Door Motion Count","-")
    r_server.set("Door Opened","-")
    r_server.set("Door Opened Count","-")

# Hallway
    print "Hallway"
    r_server.set("Hallway Light Reading",HallwayLightReading)
    print "    Hallway light: %s" % HallwayLightReading
    r_server.set("Hallway Temperature","-")
    r_server.set("Hallway Humidity","-")


    #HallwayLightReading = int(HallwayLightReading)
    if HallwayLightReading <= 50:
        r_server.set("Hallway Light Status","night time")
        print "    Hallway is night time"
    elif HallwayLightReading >= 300:
        r_server.set("Hallway Light Status","day time")
        print "    Hallway is day time"
    elif HallwayLightReading >= 600:
        r_server.set("Hallway Light Status","Hallway lights are on")
        print "    Hallway lights are on"

    global HallwayLightCommanded
    HallwayLightCommanded = r_server.get("Hallway Light Commanded")
    global HallwayBulkheadCommanded
    HallwayBulkheadCommanded = r_server.get("Hallway Bulkhead Commanded")

# Bathroom
    print "Bathroom"
    # Bathroom light
    r_server.set("Bathroom Light Reading",BathroomLightReading)

    if BathroomLightReading <= 50:
        r_server.set("Bathroom Light Status","off")
        print "    less than 50 the lights are off"
    elif BathroomLightReading >= 50:
        r_server.set("Bathroom Light Status","on")
        print "    more than 50 the lights are on"
    elif BathroomLightReading >= 700:
        r_server.set("Bathroom Light Status","shower lights")
        print "    more than 700, the shower lights are on"

    # Bathroom Temperature
    #BathroomTemperature = int(BathroomTemperature)
    r_server.set("Bathroom Temperature",BathroomTemperature)
    
    # Bathroom Humidity
    global BathroomFanStatus
    r_server.set("Bathroom Humidity",BathroomHumidity)
    if BathroomHumidity > 50:
        #jarvis_control.bathroom_fan_on()                        # turn the fan on
        r_server.set("Bathroom Fan Status","on")                 # set the redis db
        print "    Bathroom fan is on"
        BathroomFanStatus = "on"
    elif BathroomHumidity <=50:
        #jarvis_control.bathroom_fan_off()                       # turn the fan off
        r_server.set("Bathroom Fan Status","off")                 # set the redis db
        print "    Bathroom fan is off"
        BathroomFanStatus = "off"

# Hackerspace
    print "Hackerspace"
    r_server.set("Hackerspace Light Status","not set")

# Loft
    print "Loft"
    r_server.set("Loft Light Reading",LoftLightReading)
    # set the state of the loft light
    if LoftLightReading >= 50:
        r_server.set("Loft Light Status","on")
        print "    greater than 50, the loft light is on"
    elif LoftLightReading <= 51:
        r_server.set("Loft Light Status","off")
        print "    less than 50, the loft light is off"

# Bedroom

# Living Room

# Kitchen

# Water   
    print "Water"    
    # HotWater
    r_server.set("Hot Water Reading",HotWaterReading)
    if HotWaterReading >= 55:
        r_server.set("Hot Water Status","high")
        print "    the water is over 55 and is - high"
    else:
        r_server.set("Hot Water Status","normal")
        print "    the water is less than 55 - normal"
    
    # ColdWater
    r_server.set("Cold Water Reading",ColdWaterReading)
    if ColdWaterReading <= 20:
        r_server.set("Cold Water Status","on")
        print "    the water is less than 20 and is running"
    else:
        r_server.set("Cold Water Status","normal")
        print "    the cold water is not on"

    # DayElement
    r_server.set("Day Water Element Reading",DayWaterElementReading)
    if DayWaterElementReading <= 40:
        r_server.set("Day Water Element Status","off")
        print "    less than 40 and the element is off"
    else:
        r_server.set("Day Water Element Status","on")
        print "    more than 40 and the element is on"
    
    # NightElement
    r_server.set("Night Water Element Reading",NightWaterElementReading)
    if NightWaterElementReading <= 40:
        r_server.set("Night Water Element Status","off")
        print "    less than 40 and the element is off"
    else:
        r_server.set("Night Water Element Status","on")
        print "    more than 40 and the element is on"

# Power
    print "Power"
    r_server.set("Power CT1",Power_CT1)
    print "    Power 1 is: %s" % Power_CT1
    r_server.set("Power CT2",Power_CT2)
    print "    Power 2 is: %s" % Power_CT2
    r_server.set("Power CT3",Power_CT3)
    print "    Power 3 is: %s" % Power_CT3
    r_server.set("Power_CT4",Power_CT4)
    print "    Power 4 is: %s" % Power_CT4

# DEBUG

if __name__ == '__main__':
    while(1):
        bathroom()
        water()
        energy()
        redis_settings()
        print "=== Logging ==="
        # setting the csv file up to record the data
        write_date = time.strftime('%Y-%m-%d') # these are seperated because Py did not like comma between time and date
        write_time = time.strftime('%H:%M')
        filename = '/home/pi/JARVIS/records/JARVIS_monitor-%s.csv' % write_date
        with open(filename, 'a') as record:
            writer = csv.writer(record)
            writer.writerow([
                write_date,
                write_time,
                HallwayLightReading,
                HallwayLightCommanded,
                HallwayBulkheadCommanded,
                BathroomLightReading,
                #BathroomLightStatus,
                #BathroomLightCommanded,
                BathroomTemperature,
                BathroomHumidity,
                BathroomFanStatus,
                #HackerspaceLightCommanded,
                #BedroomLightCommanded,
                HotWaterReading,
                ColdWaterReading,
                DayWaterElementReading,
                NightWaterElementReading,
                Power_CT1,
                Power_CT2,
                Power_CT3,
                Power_CT4]) 
        record.close ()

"""
if __name__ == '__main__':

    bathroom()
    water()
    energy()
    redis_settings()
    print "end"
"""    