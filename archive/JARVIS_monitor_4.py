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
address_kitchen = ( '192.168.68.220', 5000)
address_bedroom = ( '192.168.1.215', 5000)
address_hackerspace = ( '192.168.1.220', 5000)

# setup the socket for the UDP packets
client_socket =socket(AF_INET, SOCK_DGRAM) #Set up the Socket
client_socket.settimeout(1) #Only wait 1 second for a response

# =============================================================
# ========================= Main Loop =========================
# =============================================================
if __name__ == '__main__':
    while(1):

# =============================================================
# ========================= Door ==============================
# =============================================================
        print "=== Door ==="    

# ========================= Door Motion =========================        
        DoorMotion = 0
        print "Door motion is: ", DoorMotion
        r_server.set("Door Motion","-")
        DoorMotionCount = 0
        print "Door motion count is: ", DoorMotionCount
        r_server.set("Door Motion Count","-")
# ========================= Door Open =========================
        DoorOpened = 0
        print "Door opened is: ", DoorOpened
        r_server.set("Door Opened","-")
        DoorOpenedCount = 0
        print "Door opened count is: ", DoorOpenedCount
        r_server.set("Door Opened Count","-")

        print "" # leave a gap before next section   

# =============================================================
# ========================= Bedroom ===========================
# =============================================================
        print "=== Bedroom ==="

# ========================= Bedroom Light =========================
        client_socket.sendto( "BedroomLight", address_bedroom) #Send the data request
        try:        
            BedroomLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "Bedroom Light is ", BedroomLightReading # print the result
            r_server.set("Bedroom Light Reading", BedroomLightReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

# ========================= Bathroom Temperature =========================
        client_socket.sendto( "BedroomTemperature", address_bedroom) #Send the data request
        try:        
            BedroomTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            BedroomTemperatureReading = float(BedroomTemperatureReading) #Convert string rec_data to float temp
            print "The temperature is ", BedroomTemperatureReading, "*C" # Print the result
            r_server.set("Bedroom Temperature Reading", BedroomTemperatureReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

# ========================= Bathroom Humidity =========================
        client_socket.sendto( "BedroomHumidity", address_bedroom) #Send the data request
        try:        
            BedroomHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            BedroomHumidityReading = float(BedroomHumidityReading) #Convert string rec_data to float temp
            print "The humidity is ", BedroomHumidityReading,"%" # Print the result
            r_server.set("Bedroom Humidity Reading", BedroomHumidityReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

        print "" # leave a gap before next section

# =============================================================
# ========================= Hackerspace =======================
# =============================================================
        print "=== Hackerspace ==="

# ========================= Hackspace Light =========================
        client_socket.sendto( "HackerspaceLight", address_hackerspace) #Send the data request
        try:        
            HackerspaceLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            HackerspaceLightReading = float(HackerspaceLightReading) #Convert string rec_data to float temp
            print "Hackerspace Light is ", HackerspaceLightReading # print the result
            r_server.set("Hackerspace Light Reading",HackerspaceLightReading)   
        except:
            pass
        time.sleep(1) #delay before sending next command

# ========================= Hackspace Motion =========================
        client_socket.sendto( "HackerspaceMotion", address_hackerspace) #Send the data request
        try:        
            HackerspaceMotionReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            HackerspaceMotionReading = float(HackerspaceMotionReading) #Convert string rec_data to float temp
            print "Hackerspace Motion is ", HackerspaceMotionReading # print the result
            r_server.set("Hackerspace Motion Reading",HackerspaceMotionReading)  
        except:
            pass
        time.sleep(1) #delay before sending next command

# ========================= Hackspace Temperature =========================
        client_socket.sendto( "HackerspaceTemperature", address_hackerspace) #Send the data request
        try:        
            HackerspaceTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            HackerspaceTemperatureReading = float(HackerspaceTemperatureReading) #Convert string rec_data to float temp
            print "Hackerspace Temperature is ", HackerspaceTemperatureReading, "*C" # print the result
            r_server.set("Hackerspace Temperature Reading",HackerspaceTemperatureReading)
        except:
            pass
        time.sleep(1) #delay before sending next command

# ========================= Hackspace Humidity =========================
        client_socket.sendto( "HackerspaceHumidity", address_hackerspace) #Send the data request 
        try:        
            HackerspaceHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            HackerspaceHumidityReading = float(HackerspaceHumidityReading) #Convert string rec_data to float temp
            print "Hackerspace Humidity is ", HackerspaceHumidityReading, "%" # print the result
            r_server.set("Hackerspace Humidity Reading",HackerspaceHumidityReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

        print "" # leave a gap before next section

# =============================================================
# ========================= Loft ==============================
# =============================================================
        print "=== Loft ==="

# ========================= Loft Light =========================
        client_socket.sendto( "LoftLight", address_bathroom) #Send the data request
        try:        
            LoftLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Loft Light is ", LoftLightReading # Print the result
            r_server.set("Loft Light Reading",LoftLightReading)
        except:
            pass
        time.sleep(1) #delay before sending next command
        
        print "" # leave a gap before next section

# =============================================================
# ========================= Hallway ===========================
# =============================================================
        print "=== Hallway ==="

# ========================= Hallway Light =========================
        client_socket.sendto( "HallwayLight", address_bathroom) #Send the data request
        try:        
            HallwayLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Hallway Light is ", HallwayLightReading # Print the result
            r_server.set("Hallway Light Reading",HallwayLightReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    
        print "" # leave a gap before next section

# =============================================================
# ========================= Bathroom ==========================
# =============================================================
        print "=== Bathroom ==="

# ========================= Bathroom Temperature =========================
        client_socket.sendto( "Temperature", address_bathroom) #Send the data request
        try:        
            BathroomTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            BathroomTemperatureReading = float(BathroomTemperatureReading) #Convert string rec_data to float temp
            print "The temperature is ", BathroomTemperatureReading, "*C" # Print the result
            r_server.set("Bathroom Temperature Reading", BathroomTemperatureReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

# ========================= Bathroom Humidity =========================
        client_socket.sendto( "Humidity", address_bathroom) #Send the data request
        try:        
            BathroomHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            BathroomHumidityReading = float(BathroomHumidityReading) #Convert string rec_data to float temp
            print "The humidity is ", BathroomHumidityReading,"%" # Print the result
            r_server.set("Bathroom Humidity Reading", BathroomHumidityReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

# ========================= Bathroom Light =========================
        client_socket.sendto( "BathroomLight", address_bathroom) #Send the data request
        try:        
            BathroomLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Bathroom Light is ", BathroomLightReading # Print the result
            r_server.set("Bathroom Light Reading", BathroomLightReading)
        except:
            pass
        time.sleep(1) #delay before sending next command 

        print "" # leave a gap before next section

# =============================================================
# ========================= Kitchen ===========================
# =============================================================
        print "=== Kitchen ==="

# ========================= Kitchen Light =========================
        client_socket.sendto( "KitchenLight", address_kitchen) #Send the data request
        try:        
            KitchenLightReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Kitchen Light is ", KitchenLightReading # Print the result
            r_server.set("Kitchen Light Reading", KitchenLightReading)
        except:
            pass
        time.sleep(1) #delay before sending next command

# ========================= Kitchen Motion =========================
        client_socket.sendto( "KitchenMotion", address_kitchen) #Send the data request
        try:        
            KitchenMotionReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Kitchen Motion is ", KitchenMotionReading # Print the result
            r_server.set("Kitchen Motion Reading", KitchenMotionReading)
        except:
            pass
        time.sleep(1) #delay before sending next command

# ========================= Kitchen Temperature =========================
        client_socket.sendto( "KitchenTemperature", address_kitchen) #Send the data request
        try:        
            KitchenTemperatureReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The temperature is ", KitchenTemperatureReading, "*C" # Print the result
            r_server.set("Kitchen Temperature Reading", KitchenTemperatureReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    

 # ========================= Kitchen Humidity =========================
        client_socket.sendto( "KitchenHumidity", address_kitchen) #Send the data request
        try:        
            KitchenHumidityReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The humidity is ", KitchenHumidityReading,"%" # Print the result
            r_server.set("Kitchen Humidity Reading", KitchenHumidityReading)
        except:
            pass
        time.sleep(1) #delay before sending next command    
        
        print "" # leave a gap before next section

# =============================================================
# ========================= Water =============================
# =============================================================
        print "=== Water ==="

# ========================= Hot Water Pipe =========================
        client_socket.sendto( "HotWater", address_energy_water) #Send the data request
        try:        
            HotWaterReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Hot water temperature is ", HotWaterReading, "*C" # print the result
            r_server.set("Hot Water Reading",HotWaterReading)
        except:
            HotWaterReading = '-'
        time.sleep(1) #delay before sending next command
# ========================= Cold Water Pipe =========================
        client_socket.sendto( "ColdWater", address_energy_water) #Send the data request
        try:        
            ColdWaterReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Cold water temperature is ", ColdWaterReading, "*C" # print the result
            r_server.set("Cold Water Reading",ColdWaterReading)
        except:
            pass
        time.sleep(1) #delay before sending next command
# ========================= Daytime Water Element =========================
        client_socket.sendto( "DayElement", address_energy_water) #Send the data request
        try:        
            DayWaterElementReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Day element Temperature is ", DayWaterElementReading, "*C" # print the result
            r_server.set("Day Water Element Reading",DayWaterElementReading)
        except:
            pass
        time.sleep(1) #delay before sending next command
# ========================= Nighttime Water Element =========================
        client_socket.sendto( "NightElement", address_energy_water) #Send the data request
        try:        
            NightWaterElementReading, addr = client_socket.recvfrom(2048) #Read response from arduino
            print "The Econ7 Temperature is ", NightWaterElementReading, "*C" # print the result
            r_server.set("Night Water Element Reading",NightWaterElementReading)
        except:
            pass
        time.sleep(1) #delay before sending next command
        
        print "" # leave a gap before next section    

# =============================================================
# ========================= Power =============================
# =============================================================
        print "=== Power ==="

# ========================= CT1 =========================
        client_socket.sendto( "CT1", address_energy_water) #Send the data request
        try:        
            Power_CT1, addr = client_socket.recvfrom(2048) #Read response from arduino
            Power_CT1 = float(Power_CT1) #Convert string rec_data to float temp
            Power_CT1 = Power_CT1/2
            print "CT1 - current consumption is", Power_CT1, "Amps rms." # print the result
            CT1_power = (Power_CT1*240)/1000
            CT1_cost = CT1_power*0.17
            CT1_cost = (round(CT1_cost,2))
            #print "Power consumpton is", CT1_power, "kWatts"
            #print "Power cost is ",CT1_cost
            r_server.set("Power CT1", Power_CT1)
        except:
            Power_CT1 = ""
        time.sleep(1) #delay before sending next command

# ========================= CT2 =========================
        client_socket.sendto( "CT2", address_energy_water) #Send the data request
        try:
            Power_CT2, addr = client_socket.recvfrom(2048) #Read response from arduino
            Power_CT2 = float(Power_CT2) #Convert string rec_data to float temp
            Power_CT2 = Power_CT2/2
            print "CT2 - current consumption is", Power_CT2, "Amps rms." # print the result
            CT2_power = (Power_CT2*240)/1000
            CT2_cost = CT2_power*0.17
            CT2_cost = (round(CT2_cost,2))
            #print "Power consumpton is", CT2_power, "kWatts"
            #print "Power cost is ",CT2_cost
            r_server.set("Power CT2", Power_CT2)
        except:
            Power_CT2 = ""
        time.sleep(1) #delay before sending next command

# ========================= CT3 =========================
        client_socket.sendto( "CT3", address_energy_water) #Send the data request
        try:
            Power_CT3, addr = client_socket.recvfrom(2048) #Read response from arduino
            Power_CT3 = float(Power_CT3) #Convert string rec_data to float temp
            Power_CT3 = Power_CT3/2
            print "CT3 - current consumption is", Power_CT3, "Amps rms." # print the result
            CT3_power = (Power_CT3*240)/1000
            CT3_cost = CT3_power*0.17
            CT3_cost = (round(CT3_cost,2))
            #print "Power consumpton is", CT3_power, "kWatts"
            #print "Power cost is ",CT3_cost
            r_server.set("Power CT3", Power_CT3)
        except:
            Power_CT3 = ""
        time.sleep(1) #delay before sending next command    

# ========================= CT4 =========================
        client_socket.sendto( "CT4", address_energy_water) #Send the data request
        try:
            Power_CT4, addr = client_socket.recvfrom(2048) #Read response from arduino
            Power_CT4 = float(Power_CT4) #Convert string rec_data to float temp
            Power_CT4 = Power_CT4/2
            print "CT4 - current consumption is", Power_CT4, "Amps rms." # print the result
            CT4_power = (Power_CT4*240)/1000
            CT4_cost = CT4_power*0.17
            CT4_cost = (round(CT4_cost,2))
            #print "Power consumpton is", CT4_power, "kWatts"
            #print "Power cost is ",CT4_cost
            r_server.set("Power CT4", Power_CT4)
        except:
            Power_CT4 = ""
        time.sleep(1) #delay before sending next command
        
        print "" # leave a gap before next section

# =============================================================
# ========================= Log ===============================
# =============================================================
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
                'HallwayLightStatus',
                'HallwayLightCommanded',
                'HallwayBulkheadCommanded',
                'HallwayTemperatureReading',
                'HallwayHumidityReading',
                
                # Bathroom
                BathroomLightReading,
                'BathroomLightStatus',
                'BathroomLightCommanded',
                BathroomTemperatureReading,
                BathroomHumidityReading,
                'BathroomFanStatus',
                
                # Hackerspace
                HackerspaceLightReading,
                'HackerspaceLightStatus',
                'HackerspaceLightCommanded',
                HackerspaceTemperatureReading,
                HackerspaceHumidityReading,

                # Loft
                LoftLightReading,
                'LoftLightStatus',
                
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
                'HotWaterStatus',
                'ColdWaterStatus',
                'DayWaterElementStatus',
                'NightWaterElementStatus',

                # Power
                Power_CT1,
                Power_CT2,
                Power_CT3,
                Power_CT4])
            record.close ()
            print "log entry made"

            print "" # leave a gap before next section
# END