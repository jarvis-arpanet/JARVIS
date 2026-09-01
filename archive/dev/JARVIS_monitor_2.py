#!/usr/bin/env python3

# import the libraries
from socket import *
import time
import csv # this is to write the results to a comma seperated value file
import redis

# set the redis server and functions
r_server = redis.Redis("localhost")

# set the IP addresses of the Arduinos
address_energy_water = ( '192.168.1.210', 5000)
address_bathroom = ( '192.168.1.235', 5000)
address_kitchen = ( '192.168.1.225', 5000)
address_bedroom = ( '192.168.1.215', 5000)
address_hackerspace = ( '192.168.1.220', 5000)

# setup the socket for the UDP packets
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

def bedroom():
    print "=== Bedroom ==="
# ========================= Bedroom Light =========================
    client_socket.sendto( "BedroomLight", address_bedroom) #Send the data request
    try:
        global BedroomLightReading
        BedroomLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        BedroomLightReading = float(BedroomLightReading) #Convert string rec_data to float temp
        print "Bedroom Light is ", BedroomLightReading # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    
# ========================= Bathroom Temperature =========================
    client_socket.sendto( "BedroomTemperature", address_bedroom) #Send the data request
    try:
        global BedroomTemperatureReading
        BedroomTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        BedroomTemperatureReading = float(BedroomTemperatureReading) #Convert string rec_data to float temp
        print "The temperature is ", BedroomTemperatureReading, "*C" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    
# ========================= Bathroom Humidity =========================
    client_socket.sendto( "BedroomHumidity", address_bedroom) #Send the data request
    try:
        global BedroomHumidityReading
        BedroomHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        BedroomHumidityReading = float(BedroomHumidityReading) #Convert string rec_data to float temp
        print "The humidity is ", BedroomHumidityReading,"%" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    

    print ""

def hackerspace():
    print "=== Hackerspace ==="
# ========================= Hackspace Light =========================
    client_socket.sendto( "HackerspaceLight", address_hackerspace) #Send the data request
    try:
        global HackerspaceLightReading
        HackerspaceLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        HackerspaceLightReading = float(HackerspaceLightReading) #Convert string rec_data to float temp
        print "Hackerspace Light is ", HackerspaceLightReading # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Motion =========================
    client_socket.sendto( "HackerspaceMotion", address_hackerspace) #Send the data request
    try:
        global HackerspaceMotionReading
        HackerspaceMotionReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        HackerspaceMotionReading = float(HackerspaceMotionReading) #Convert string rec_data to float temp
        print "Hackerspace Motion is ", HackerspaceMotionReading # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Temperature =========================
    client_socket.sendto( "HackerspaceTemperature", address_hackerspace) #Send the data request
    try:
        global HackerspaceTemperatureReading
        HackerspaceTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        HackerspaceTemperatureReading = float(HackerspaceTemperatureReading) #Convert string rec_data to float temp
        print "Hackerspace Temperature is ", HackerspaceTemperatureReading, " C" # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Hackspace Humidity =========================
    client_socket.sendto( "HackerspaceHumidity", address_hackerspace) #Send the data request 
    try:
        global HackerspaceHumidityReading
        HackerspaceHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        HackerspaceHumidityReading = float(HackerspaceHumidityReading) #Convert string rec_data to float temp
        print "Hackerspace Humidity is ", HackerspaceHumidityReading, " %" # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    

    print ""

def bathroom():
    print "=== Bathroom ==="
# ========================= Bathroom Temperature =========================
    client_socket.sendto( "Temperature", address_bathroom) #Send the data request
    try:
        global BathroomTemperatureReading
        BathroomTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        BathroomTemperatureReading = float(BathroomTemperatureReading) #Convert string rec_data to float temp
        print "The temperature is ", BathroomTemperatureReading, "*C" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    
# ========================= Bathroom Humidity =========================
    client_socket.sendto( "Humidity", address_bathroom) #Send the data request
    try:
        global BathroomHumidityReading
        BathroomHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        BathroomHumidityReading = float(BathroomHumidityReading) #Convert string rec_data to float temp
        print "The humidity is ", BathroomHumidityReading,"%" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    

# ========================= Bathroom Light =========================
    client_socket.sendto( "BathroomLight", address_bathroom) #Send the data request
    try:
        global BathroomLightReading
        BathroomLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Bathroom Light is ", BathroomLightReading # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command 
    print ""

    print "=== Loft ==="
# ========================= Loft Light =========================
    client_socket.sendto( "LoftLight", address_bathroom) #Send the data request
    try:
        global LoftLightReading
        LoftLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Loft Light is ", LoftLightReading # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command
    print ""

    print "=== Hallway ==="
# ========================= Hallway Light =========================
    client_socket.sendto( "HallwayLight", address_bathroom) #Send the data request
    try:
        global HallwayLightReading
        HallwayLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Hallway Light is ", HallwayLightReading # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    
    print ""

def kitchen():
    print "=== Kitchen ==="
# ========================= Kitchen Light =========================
    client_socket.sendto( "KitchenLight", address_kitchen) #Send the data request
    try:
        global KitchenLightReading
        KitchenLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Kitchen Light is ", KitchenLightReading # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Kitchen Motion =========================
    client_socket.sendto( "KitchenMotion", address_kitchen) #Send the data request
    try:
        global KitchenMotionReading
        KitchenMotionReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Kitchen Motion is ", KitchenMotionReading # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command

# ========================= Kitchen Temperature =========================
    client_socket.sendto( "KitchenTemperature", address_kitchen) #Send the data request
    try:
        global KitchenTemperatureReading
        KitchenTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The temperature is ", KitchenTemperatureReading, "*C" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    

# ========================= Kitchen Humidity =========================
    client_socket.sendto( "KitchenHumidity", address_kitchen) #Send the data request
    try:
        global KitchenHumidityReading
        KitchenHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The humidity is ", KitchenHumidityReading,"%" # Print the result
    except:
        pass
    time.sleep(1) #delay before sending next command    
    print ""

def water():
    print "=== Water ==="
# ========================= Hot Water Pipe =========================
    client_socket.sendto( "HotWater", address_energy_water) #Send the data request
    try:
        global HotWaterReading
        HotWaterReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Hot water temperature is ", HotWaterReading, " degrees C." # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command
# ========================= Cold Water Pipe =========================
    client_socket.sendto( "ColdWater", address_energy_water) #Send the data request
    try:
        global ColdWaterReading
        ColdWaterReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Cold water temperature is ", ColdWaterReading, " degrees C." # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command
# ========================= Daytime Water Element =========================
    client_socket.sendto( "DayElement", address_energy_water) #Send the data request
    try:
        global DayWaterElementReading
        DayWaterElementReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Day element Temperature is ", DayWaterElementReading, " degrees C." # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command
# ========================= Nighttime Water Element =========================
    client_socket.sendto( "NightElement", address_energy_water) #Send the data request
    try:
        global NightWaterElementReading
        NightWaterElementReading, addr = client_socket.recvfrom(2048) #Read response from arduino
        print "The Econ7 Temperature is ", NightWaterElementReading, " degrees C." # print the result
    except:
        pass
    time.sleep(1) #delay before sending next command
    print ""    

def energy():
    print "=== Power ==="
# ========================= CT1 =========================
    client_socket.sendto( "CT1", address_energy_water) #Send the data request
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
    time.sleep(1) #delay before sending next command
# ========================= CT2 =========================
    client_socket.sendto( "CT2", address_energy_water) #Send the data request
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
    time.sleep(1) #delay before sending next command
# ========================= CT3 =========================
    client_socket.sendto( "CT3", address_energy_water) #Send the data request
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
    time.sleep(1) #delay before sending next command    
# ========================= CT4 =========================
    client_socket.sendto( "CT4", address_energy_water) #Send the data request
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
    time.sleep(1) #delay before sending next command
    print ""    

def status_settings():
# Door
    global DoorMotion
    DoorMotion = 'not set'
    global DoorMotionCount
    DoorMotionCount = 'not set'
    global DoorOpened
    DoorOpened = 'not set'
    global DoorOpenedCount
    DoorOpenedCount = 'not set'

# Hallway
    global HallwayLightStatus
    HallwayLightStatus = 'not set'

# Bathroom
    global BathroomLightStatus
    BathroomLightStatus = 'not set'
    global BathroomFanStatus
    BathroomFanStatus = 'not set'

# Hackerspace
    global HackerspaceLightStatus
    HackerspaceLightStatus = 'not set'

# Loft
    global LoftLightStatus
    LoftLightStatus = 'not set'

# Bedroom

# Living Room

# Kitchen

# Water
    # HotWater
    global HotWaterStatus
    r_server.set("Hot Water Reading",HotWaterReading)
    if HotWaterReading >= 55:
        r_server.set("Hot Water Status","high")                         # the water is over 55 and is - high
        HotWaterStatus = "high"
    else:
        r_server.set("Hot Water Status","normal")                       # the water is less than 55 - normal
        HotWaterStatus = "normal"
    
    # ColdWater
    global ColdWaterStatus
    r_server.set("Cold Water Reading",ColdWaterReading)
    if ColdWaterReading <= 20:
        r_server.set("Cold Water Status","on")                          # the water is less than 20 and is running
        ColdWaterStatus = "on"
    else:
        r_server.set("Cold Water Status","normal")                      # the cold water is not on
        ColdWaterStatus = "normal"
    
    # DayElement
    global DayWaterElementStatus
    r_server.set("Day Water Element Reading",DayWaterElementReading)
    if DayWaterElementReading <= 40:
        r_server.set("Day Water Element Status","off")                  # less than 40 and the element is off
        DayWaterElementStatus = 'off'
    else:
        r_server.set("Day Water Element Status","on")                   # more than 40 and the element is on   
        DayWaterElementStatus = 'on'

    # NightElement
    global NightWaterElementStatus
    r_server.set("Night Water Element Reading",NightWaterElementReading)
    if NightWaterElementReading <= 40:
        r_server.set("Night Water Element Status","off")                # less than 40 and the element is off
        NightWaterElementStatus = 'off'
    else:
        r_server.set("Night Water Element Status","on")                 # more than 40 and the element is on
        NightWaterElementStatus = 'on'

# Power

def redis_settings():
    print "=== Redis ==="    
# ========================= Redis =========================

# Door
    r_server.set("Door Motion","-")
    r_server.set("Door Motion Count","-")
    r_server.set("Door Opened","-")
    r_server.set("Door Opened Count","-")

# Hallway
    r_server.set("Hallway Light Reading",HallwayLightReading)
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

    global HallwayTemperatureReading
    HallwayTemperatureReading = 'not set'
    global HallwayHumidityReading
    HallwayHumidityReading = 'not set'

# Bathroom
    # Bathroom light
    r_server.set("Bathroom Light Reading",BathroomLightReading)
    global BathroomLightCommanded
    BathroomLightCommanded = 'not set'

    if BathroomLightReading <= 50:
        r_server.set("Bathroom Light Status","off")                     # less than 50 the lights are off
    elif BathroomLightReading >= 50:
        r_server.set("Bathroom Light Status","on")                       # more than 50 the lights are on
    elif BathroomLightReading >= 700:
        r_server.set("Bathroom Light Status","shower lights")             # more than 700, the shower lights are on

    # Bathroom Temperature
    #BathroomTemperature = int(BathroomTemperature)
    r_server.set("Bathroom Temperature Reading",BathroomTemperatureReading)
    
    # Bathroom Humidity
    r_server.set("Bathroom Humidity Reading",BathroomHumidityReading)

# Hackerspace
    #global HackerspaceLightReading
    global HackerspaceLightStatus
    global HackerspaceLightCommanded
    #global HackerspaceTemperatureReading
    #global HackerspaceHumidityReading

    #HackerspaceLightReading = 'not set'
    HackerspaceLightStatus = 'not set'
    HackerspaceLightCommanded = 'not set'
    #HackerspaceTemperatureReading = 'not set'
    #HackerspaceHumidityReading = 'not set'
    
    r_server.set("Hackerspace Light Reading",HackerspaceLightReading)
    r_server.set("Hackerspace Light Status","not set")
    r_server.set("Hackerspace Light Commanded","not set")
    r_server.set("Hackerspace Temperature Reading",HackerspaceTemperatureReading)
    r_server.set("Hackerspace Humidity Reading",HackerspaceHumidityReading)
    r_server.set("Hackerspace Motion Reading",HackerspaceMotionReading)    

# Loft
    r_server.set("Loft Light Reading",LoftLightReading)
    # set the state of the loft light
    if LoftLightReading >= 50:
        r_server.set("Loft Light Status","on")                          # greater than 50, the loft light is on
    elif LoftLightReading <= 51:
        r_server.set("Loft Light Status","off")                         # less than 50, the loft light is off

# Bedroom
    r_server.set("Bedroom Light Reading", BedroomLightReading)
    r_server.set("Bedroom Temperature Reading", BedroomTemperatureReading)
    r_server.set("Bedroom Humidity Reading", BedroomHumidityReading)

# Living Room

# Kitchen
    r_server.set("Kitchen Light Reading", KitchenLightReading)
    r_server.set("Kitchen Temperature Reading", KitchenTemperatureReading)
    r_server.set("Kitchen Humidity Reading", KitchenHumidityReading)
    r_server.set("Kitchen Motion Reading", KitchenMotionReading)

# Water    
    # HotWater
    global HotWaterStatus
    r_server.set("Hot Water Reading",HotWaterReading)
    if HotWaterReading >= 55:
        r_server.set("Hot Water Status","high")                         # the water is over 55 and is - high
        HotWaterStatus = "high"
    else:
        r_server.set("Hot Water Status","normal")                       # the water is less than 55 - normal
        HotWaterStatus = "normal"
    # ColdWater
    global ColdWaterStatus
    r_server.set("Cold Water Reading",ColdWaterReading)
    if ColdWaterReading <= 20:
        r_server.set("Cold Water Status","on")                          # the water is less than 20 and is running
        ColdWaterStatus = "on"
    else:
        r_server.set("Cold Water Status","normal")                      # the cold water is not on
        ColdWaterStatus = "normal"
    # DayElement
    r_server.set("Day Water Element Reading",DayWaterElementReading)
    if DayWaterElementReading <= 40:
        r_server.set("Day Water Element Status","off")                  # less than 40 and the element is off
    else:
        r_server.set("Day Water Element Status","on")                   # more than 40 and the element is on   
    # NightElement
    r_server.set("Night Water Element Reading",NightWaterElementReading)
    if NightWaterElementReading <= 40:
        r_server.set("Night Water Element Status","off")                # less than 40 and the element is off
    else:
        r_server.set("Night Water Element Status","on")                 # more than 40 and the element is on

# Power
    r_server.set("Power CT1", Power_CT1)
    r_server.set("Power CT2", Power_CT2)
    r_server.set("Power CT3", Power_CT3)
    r_server.set("Power CT4", Power_CT4)

# DEBUG
    print ""

# ========================= Main Loop =========================
if __name__ == '__main__':
    while(1):
        bedroom()
        kitchen()
        hackerspace()
        bathroom()
        water()
        energy()        
        status_settings()
        redis_settings()
# Generating the Comma Seperated Value file
        print "=== Logging ==="
        write_date = time.strftime('%Y-%m-%d') # these are seperated because Py did not like comma between time and date
        write_time = time.strftime('%H:%M')
        filename = '/home/pi/JARVIS/records/JARVIS_monitor-%s.csv' % write_date
        # write the data to the file
        with open(filename, 'a') as record:
            writer = csv.writer(record)
            writer.writerow([
                write_date,
                write_time,
                
                # Door
                DoorMotion,
                DoorMotionCount,
                DoorOpened,
                DoorOpenedCount,

                # Hallway
                HallwayLightReading,
                HallwayLightStatus,
                HallwayLightCommanded,
                HallwayBulkheadCommanded,
                HallwayTemperatureReading,
                HallwayHumidityReading,
                
                # Bathroom
                BathroomLightReading,
                BathroomLightStatus,
                BathroomLightCommanded,
                BathroomTemperatureReading,
                BathroomHumidityReading,
                BathroomFanStatus,
                
                # Hackerspace
                HackerspaceLightReading,
                HackerspaceLightStatus,
                HackerspaceLightCommanded,
                HackerspaceTemperatureReading,
                HackerspaceHumidityReading,

                # Loft
                LoftLightReading,
                LoftLightStatus,
                
                # Bedroom
                BedroomLightReading,
                BedroomTemperatureReading,
                BedroomHumidityReading,

                # Living Room

                # Kitchen
                KitchenLightReading,
                KitchenTemperatureReading,
                KitchenHumidityReading,
                KitchenMotionReading,

                # Water
                HotWaterReading,
                ColdWaterReading,
                DayWaterElementReading,
                NightWaterElementReading,
                HotWaterStatus,
                ColdWaterStatus,
                DayWaterElementStatus,
                NightWaterElementStatus,

                # Power
                Power_CT1,
                Power_CT2,
                Power_CT3,
                Power_CT4])
        print "logging completed"
        print ""
        record.close ()
# END