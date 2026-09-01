import redis

r_server = redis.Redis("localhost")

# Door
DoorMotion = r_server.get("Door Motion")
DoorMotionCount = r_server.get("Door Motion Count")
DoorOpened = r_server.get("Door Opened")
DoorOpenedCount = r_server.get("Door Opened Count")

# Hallway
HallwayLightReading = r_server.get("Hallway Light Reading")
HallwayLightStatus = r_server.get("Hallway Light Status")
HallwayLightCommanded = r_server.get("Hallway Light Commanded")
HallwayBulkheadCommanded = r_server.get("Hallway Bulkhead Commanded")
HallwayTemperatureReading = r_server.get("Hallway Temperature Reading")
HallwayHumidityReading = r_server.get("Hallway Humidity Reading")

# Bathroom
BathroomLightReading = r_server.get("Bathroom Light Reading")
BathroomLightStatus = r_server.get("Bathroom Light Status")
BathroomLightCommanded = r_server.get("Bathroom Light Commanded")
BathroomTemperatureReading = r_server.get("Bathroom Temperature Reading")
BathroomHumidityReading = r_server.get("Bathroom Humidity Reading")
BathroomFanStatus = r_server.get("Bathroom Fan Status")

# Hackerspace
HackerspaceLightReading = r_server.get("Hackerspace Light Reading")
HackerspaceLightStatus = r_server.get("Hackerspace Light Status")
HackerspaceLightCommanded = r_server.get("Hackerspace Light Commanded")
HackerspaceTemperatureReading = r_server.get("Hackerspace Temperature Reading")
HackerspaceHumidityReading = r_server.get("Hackerspace Humidity Reading")
HackerspaceMotionReading = r_server.get("Hackerspace Motion Reading")  

# Loft
LoftLightReading = r_server.get("Loft Light Reading")
LoftLightStatus = r_server.get("Loft Light Status")

# Bedroom
BedroomLightCommanded = r_server.get("Bedroom Light Commanded")
BedroomLightReading = r_server.get("Bedroom Light Reading")
BedroomTemperatureReading = r_server.get("Bedroom Temperature Reading")
BedroomHumidityReading = r_server.get("Bedroom Humidity Reading")

# Living Room

# Kitchen
KitchenLightReading = r_server.get("Kitchen Light Reading")
KitchenTemperatureReading = r_server.get("Kitchen Temperature Reading")
KitchenHumidityReading = r_server.get("Kitchen Humidity Reading")
KitchenMotionReading = r_server.get("Kitchen Motion Reading")

# Water
HotWaterReading = r_server.get("Hot Water Reading")
ColdWaterReading = r_server.get("Cold Water Reading")
DayWaterElementReading = r_server.get("Day Water Element Reading")
NightWaterElementReading = r_server.get("Night Water Element Reading")
HotWaterStatus = r_server.get("Hot Water Status")
ColdWaterStatus = r_server.get("Cold Water Status")
DayWaterElementStatus = r_server.get("Day Water Element Status")
NightWaterElementStatus = r_server.get("Night Water Element Status")

# Power
Power_CT1 = r_server.get("Power CT1")
Power_CT2 = r_server.get("Power CT2")
Power_CT3 = r_server.get("Power CT3")
Power_CT4 = r_server.get("Power CT4")

# Debug	


###########################################################

# Door
print "=== Door ==="
print "Time there was last motion outside: ", DoorMotion
print "Motion count: ", DoorMotionCount
print "Time door was last opened: ", DoorOpened
print "Door open count: ", DoorOpenedCount
print ""

# Hallway
print "=== Hallway ==="
print "Light reading: ", HallwayLightReading
print "Light: ", HallwayLightStatus
print "Commanded status of hallway light: ", HallwayLightCommanded
print "Commanded status of bulkhead light: ", HallwayBulkheadCommanded
print "Temperature: ", HallwayTemperatureReading
print "Humidity: ", HallwayHumidityReading
print ""

# Bathroom
print "=== Bathroom ==="
print "Light reading: ", BathroomLightReading
print "Light status: ", BathroomLightStatus
print "Light commanded", BathroomLightCommanded
print "Temperature", BathroomTemperatureReading
print "Humidty", BathroomHumidityReading
print "Fan", BathroomFanStatus
print ""

# Hackerspace
print "=== Hackerspace ==="
print "Light: ", HackerspaceLightReading
print "Light Status: ", HackerspaceLightStatus
print "Light commanded: ", HackerspaceLightCommanded
print "Temperature: ", HackerspaceTemperatureReading
print "Humidty: ", HackerspaceHumidityReading
print "Motion: ", HackerspaceMotionReading
print ""

# Loft
print "=== Loft ==="
print "Light reading: ", LoftLightReading
print "Light: ", LoftLightStatus
print ""

# Bedroom
print "=== Bedroom ==="
print "Light commanded: ", BedroomLightCommanded
print "Light: ", BedroomLightReading
print "Temperature: ", BedroomTemperatureReading
print "Humidity: ", BedroomHumidityReading
print ""

# Living Room
print "=== Living Room ==="
print ""

# Kitchen
print "=== Kitchen ==="
print "KitchenLight: ", KitchenLightReading
print "KitchenTemperature: ", KitchenTemperatureReading
print "KitchenHumidity: ", KitchenHumidityReading
print "KitchenMotion: ", KitchenMotionReading
print ""

# Water
print "=== Water ==="
print "Hot water reading: ", HotWaterReading
print "Cold water reading: ", ColdWaterReading
print "Day element reading: ", DayWaterElementReading
print "Night element reading: ", NightWaterElementReading
print "Hot water: ", HotWaterStatus
print "Cold water: ", ColdWaterStatus
print "Day element: ", DayWaterElementStatus
print "Night element: ", NightWaterElementStatus
print ""

# Power
print "=== Power ==="
print "Power on CT1: ", Power_CT1
print "Power on CT2: ", Power_CT2
print "Power on CT3: ", Power_CT3
print "Power on CT4: ", Power_CT4
print ""

# Debug	
print "=== DEBUG ==="
print ""