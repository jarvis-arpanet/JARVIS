"""
phrases explained
- commanded = where the last command was sent from, the web app or Alexa
- status = an estimation, based on the data e.g. light level above a number means the light is on

"""
import redis

r_server = redis.Redis("localhost")

# Door
r_server.set("Door Motion","last time motion detected")
r_server.set("Door Motion Count","motion detected count")
r_server.set("Door Opened","last time the door was opened")
r_server.set("Door Opened Count","door opened count")

# Hallway
r_server.set("Hallway Light Reading","not set")
r_server.set("Hallway Light Status","not set")
r_server.set("Hallway Light Commanded","not set")
r_server.set("Hallway Bulkhead Commanded","not set")
r_server.set("Hallway Temperature","not set")
r_server.set("Hallway Humidity","not set")

# Bathroom
r_server.set("Bathroom Light Reading","not set")
r_server.set("Bathroom Light Status","not set")
r_server.set("Bathroom Light Commanded","not set")
r_server.set("Bathroom Temperature","not set")
r_server.set("Bathroom Humidity","not set")
r_server.set("Bathroom Fan Status","not set")

# Hackerspace
r_server.set("Hackerspace Light Reading","not set")
r_server.set("Hackerspace Light Status","not set")
r_server.set("Hackerspace Light Commanded","not set")
r_server.set("Hackerspace Temperature Reading","not set")
r_server.set("Hackerspace Humidity Reading","not set")
r_server.set("Hackerspace Motion Reading","not set")

# Loft
r_server.set("Loft Light Reading","not set")
r_server.set("Loft Light Status","not set")

# Bedroom
r_server.set("Bedroom Light Commanded","not set")
r_server.set("Bedroom Light Reading","not set")
r_server.set("Bedroom Temperature Reading","not set")
r_server.set("Bedroom Humidity Reading","not set")
r_server.set("Bedroom Motion Reading","not set")

# Living Room
r_server.set("Livingroom Light","not set")

# Kitchen
r_server.set("Kitchen Light Reading","not set")
r_server.set("Kitchen Temperature Reading","not set")
r_server.set("Kitchen Humidity Reading","not set")
r_server.set("Kitchen Motion Reading","not set")

# Water
r_server.set("Hot Water Reading","not set")
r_server.set("Cold Water Reading","not set")
r_server.set("Day Water Element Reading","not set")
r_server.set("Night Water Element Reading","not set")
r_server.set("Hot Water Status","not set")
r_server.set("Cold Water Status","not set")
r_server.set("Day Water Element Status","not set")
r_server.set("Night Water Element Status","not set")

# Power
r_server.set("Power CT1","not set")
r_server.set("Power CT2","not set")
r_server.set("Power CT3","not set")
r_server.set("Power CT4","not set")

# Debug	
r_server.set("Test Data","this is test data")