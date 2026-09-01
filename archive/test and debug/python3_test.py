#!/usr/bin/env python3

from socket import *
import time
import csv  # this is to write the results to a comma seperated value file

#address = ('192.168.68.220', 5000)  # define server IP and port
address_kitchen = ( '192.168.68.220', 5000)
client_socket = socket(AF_INET, SOCK_DGRAM)  # Set up the Socket
client_socket.settimeout(1)  # Only wait 1 second for a response

while (1):

    # =============================================================
    # ========================= Kitchen ===========================
    # =============================================================
    print ("=== Kitchen ===")

    # ========================= Kitchen Light =========================
    client_socket.sendto(b"KitchenLight", address_kitchen)  # Send the data request
    try:
        KitchenLightReading, addr = client_socket.recvfrom(2048)  # Read response from arduino
        KitchenLightReading = float(KitchenLightReading)
        print("The Kitchen Light is ", KitchenLightReading) # Print the result

    except:
        pass
    time.sleep(1)  # delay before sending next command

    # ========================= Kitchen Motion =========================
    client_socket.sendto(b"KitchenMotion", address_kitchen)  # Send the data request
    try:
        KitchenMotionReading, addr = client_socket.recvfrom(2048)  # Read response from arduino
        KitchenMotionReading = float(KitchenMotionReading)
        print ("The Kitchen Motion is ", KitchenMotionReading)  # Print the result

    except:
        pass
    time.sleep(1)  # delay before sending next command

    # ========================= Kitchen Temperature =========================
    client_socket.sendto(b"KitchenTemperature", address_kitchen)  # Send the data request
    try:
        KitchenTemperatureReading, addr = client_socket.recvfrom(2048)  # Read response from arduino
        KitchenTemperatureReading = float(KitchenTemperatureReading)
        print ("The temperature is ", KitchenTemperatureReading, "*C") # Print the result

    except:
        pass
    time.sleep(1)  # delay before sending next command

    # ========================= Kitchen Humidity =========================
    client_socket.sendto(b"KitchenHumidity", address_kitchen)  # Send the data request
    try:
        KitchenHumidityReading, addr = client_socket.recvfrom(2048)  # Read response from arduino
        KitchenHumidityReading = float(KitchenHumidityReading)
        print ("The humidity is ", KitchenHumidityReading, "%")  # Print the result

    except:
        pass

    # ========================= end =========================
    print ("")  # leave a space before starting to read all the data again
    time.sleep(60)  # only check every minute

    # =============================================================
    # ========================= Log ===============================
    # =============================================================
    print
    "=== Logging ==="

    write_date = time.strftime('%Y-%m-%d')  # these are seperated because Py did not like comma between time and date
    write_time = time.strftime('%H:%M')
    filename = '/home/control/JARVIS/records/JARVIS_monitor-%s.csv' % write_date

    # write the data to the file
    with open(filename, 'a') as record:
        writer = csv.writer(record)
        writer.writerow([
            write_date,
            write_time,

            # Kitchen
            KitchenLightReading,
            KitchenTemperatureReading,
            KitchenHumidityReading,
            KitchenMotionReading
        ])
        record.close()
        print ("log entry made")

        print ("") # leave a gap before next section
# END