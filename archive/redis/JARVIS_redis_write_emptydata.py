"""
phrases explained
- commanded = where the last command was sent from, the web app or Alexa
- status = an estimation, based on the data e.g. light level above a number means the light is on

"""
import redis

r_server = redis.Redis("localhost")

# Door
r_server.set("Door Motion","")
r_server.set("Door Motion Count","")
r_server.set("Door Opened","")
r_server.set("Door Opened Count","")

# Hallway
r_server.set("Hallway Light Reading","")
r_server.set("Hallway Light Status","")
r_server.set("Hallway Light Commanded","")
r_server.set("Hallway Bulkhead Commanded","")
r_server.set("Hallway Temperature","")
r_server.set("Hallway Humidity","")

# Bathroom
r_server.set("Bathroom Light Reading","")
r_server.set("Bathroom Light Status","")
r_server.set("Bathroom Light Commanded","")
r_server.set("Bathroom Temperature","")
r_server.set("Bathroom Humidity","")
r_server.set("Bathroom Fan Status","")

# Hackerspace
r_server.set("Hackerspace Light Status","")
r_server.set("Hackerspace Light Commanded","")

# Loft
r_server.set("Loft Light Reading","")
r_server.set("Loft Light Status","")

# Bedroom
r_server.set("Bedroom Light Commanded","")

# Living Room
r_server.set("Livingroom Light","")

# Kitchen
r_server.set("Kitchen Light Reading","")
r_server.set("Kitchen Temperature Reading","")
r_server.set("Kitchen Humidity Reading","")
r_server.set("Kitchen Motion Reading","")

# Water
r_server.set("Hot Water Reading","")
r_server.set("Cold Water Reading","")
r_server.set("Day Water Element Reading","")
r_server.set("Night Water Element Reading","")
r_server.set("Hot Water Status","")
r_server.set("Cold Water Status","")
r_server.set("Day Water Element Status","")
r_server.set("Night Water Element Status","")

# Power
r_server.set("Power CT1","")
r_server.set("Power CT2","")
r_server.set("Power CT3","")
r_server.set("Power CT4","")

# Debug	
r_server.set("Test Data","this is test data")