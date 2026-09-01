from flask import Flask, render_template, request, redirect
import redis
from thing import PiThing
from jarvis_control import jarvis_control
import jarvis_control_2

r_server = redis.Redis("localhost")

# Create flask app and global pi 'thing' object.
app = Flask(__name__)
#pi_thing = thing.PiThing()
pi_thing = PiThing()
jarvis_control = jarvis_control()
control = jarvis_control_2.jarvis_control_2()

@app.route("/blank")
def hello():
    return "Hello World!"

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():  
    # Render index.html template.
    return render_template('index.html', switch=switch)


@app.route("/readings")
def readings(): 

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
    HallwayTemperature = r_server.get("Hallway Temperature")
    HallwayHumidity = r_server.get("Hallway Humidity")

    # Bathroom
    BathroomLightReading = r_server.get("Bathroom Light Reading")
    BathroomLightStatus = r_server.get("Bathroom Light Status")
    BathroomLightCommanded = r_server.get("Bathroom Light Commanded")
    BathroomTemperature = r_server.get("Bathroom Temperature")
    BathroomHumidity = r_server.get("Bathroom Humidity")
    BathroomFanStatus = r_server.get("Bathroom Fan Status")

    # Hackerspace
    HackerspaceLightStatus = r_server.get("Hackerspace Light Status")
    HackerspaceLightCommanded = r_server.get("Hackerspace Light Commanded")

    # Loft
    LoftLightReading = r_server.get("Loft Light Reading")
    LoftLightStatus = r_server.get("Loft Light Status")

    # Bedroom
    BedroomLightCommanded = r_server.get("Bedroom Light Commanded")

    # Living Room
    LivingroomLight = r_server.get("Living room Light")

    # Kitchen
    KitchenLight = r_server.get("Kitchen Light")

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


    dict = {
    # Door
        'Door - Time there was last motion outside':DoorMotion,
        'door Motion count':DoorMotionCount,
        'Time door was last opened':DoorOpened,
        'door open count':DoorOpenedCount,

    # Hallway
        'Hallway Light Reading':HallwayLightReading,
        'Hallway Light Status':HallwayLightStatus,
        'Commanded status of hallway light':HallwayLightCommanded,
        'Commanded status of bulkhead light':HallwayBulkheadCommanded,
        'Hallway Temperature':HallwayTemperature,
        'Hallway Humidity':HallwayHumidity,

    # Bathroom
        'bathroom Light reading':BathroomLightReading,
        'bathroom Light':BathroomLightStatus,
        'Light commanded':BathroomLightCommanded,
        'Temperature':BathroomTemperature,
        'Humidty':BathroomHumidity,
        'Fan':BathroomFanStatus,

    # Hackerspace
        'Light':HackerspaceLightStatus,
        'Light commanded':HackerspaceLightCommanded,

    # Loft
        'Light reading':LoftLightReading,
        'Light':LoftLightStatus,

    # Bedroom
        'Light commanded':BedroomLightCommanded,

    # Living Room
        'Light':LivingroomLight,

    # Kitchen
        'Light':KitchenLight,

    # Water
        'Hot Water Reading':HotWaterReading,
        'Cold Water Reading':ColdWaterReading,
        'Day Water Element Reading':DayWaterElementReading,
        'Night Water Element Reading':NightWaterElementReading,
        'Hot water':HotWaterStatus,
        'Cold water':ColdWaterStatus,
        'Day element':DayWaterElementStatus,
        'Night element':NightWaterElementStatus,

    # Power
        'Power on CT1':Power_CT1,
        'Power on CT2':Power_CT2,
        'Power on CT3':Power_CT3,
        'Power on CT4':Power_CT4}


    return render_template('readings.html', result = dict)
#return render_template('jarvis.html', result = dict)    

# LED route allows changing the LED state with a POST request.
@app.route("/led/<int:state>", methods=['POST'])
def led(state):
    # Check if the led state is 0 (off) or 1 (on) and set the LED accordingly.
    if state == 0:
        pi_thing.set_led(False)
    elif state == 1:
        pi_thing.set_led(True)
    else:
        return ('Unknown LED state', 400)
    return ('', 204)

# Door

# Hallway
@app.route("/hallway_light_on", methods=['POST'])
def hallway_light_on(): 
    control.hallway_light_on()

@app.route("/hallway_light_off", methods=['POST'])
def hallway_light_off(): 
    control.hallway_light_off()

@app.route("/bulkhead_light_on", methods=['POST'])
def bulkhead_light_on(): 
    control.bulkhead_light_on()

@app.route("/bulkhead_light_off", methods=['POST'])
def bulkhead_light_off(): 
    control.bulkhead_light_off()  

# Bathroom
@app.route("/bathroom_light_on", methods=['POST'])
def bathroom_light_on(): 
    control.bathroom_light_on()

@app.route("/bathroom_light_off", methods=['POST'])
def bathroom_light_off(): 
    control.bathroom_light_off()

@app.route("/bathroom_fan_on", methods=['POST'])
def bathroom_fan_on(): 
    control.bathroom_fan_on()

@app.route("/bathroom_fan_off", methods=['POST'])
def bathroom_fan_off(): 
    control.bathroom_fan_off()

# Hackerspace
@app.route("/hackerspace_desk_on", methods=['POST'])
def hackerspace_desk_on():
    control.hackerspace_desk_on()

@app.route("/hackerspace_desk_off", methods=['POST'])
def hackerspace_desk_off(): 
    control.hackerspace_desk_off()

@app.route("/hackerspace_lights_on", methods=['POST'])
def hackerspace_lights_on():
    control.hackerspace_lights_on()

@app.route("/hackerspace_lights_off", methods=['POST'])
def hackerspace_lights_off(): 
    control.hackerspace_lights_off()

# Loft

# Bedroom
@app.route("/bedroom_lamp_on", methods=['POST'])
def bedroom_lamp_on(): 
    control.bedroom_lamp_on()

@app.route("/bedroom_lamp_off", methods=['POST'])
def bedroom_lamp_off(): 
    control.bedroom_lamp_off()

@app.route("/bedroom_hair_on", methods=['POST'])
def bedroom_hair_on(): 
    control.bedroom_hair_on()

@app.route("/bedroom_hair_off", methods=['POST'])
def bedroom_hair_off(): 
    control.bedroom_hair_off()

# Living Room
@app.route("/alexa_speaker_on", methods=['POST'])
def alexa_speaker_on():
    control.alexa_speaker_on()

@app.route("/alexa_speaker_off", methods=['POST'])
def alexa_speaker_off(): 
    control.alexa_speaker_off()

@app.route("/tv_on", methods=['POST'])
def tv_on():
    control.tv_on()

@app.route("/tv_off", methods=['POST'])
def tv_off(): 
    control.tv_off()

@app.route("/living_room_lamp_on", methods=['POST'])
def living_room_lamp_on():
    control.living_room_lamp_on()

@app.route("/living_room_lamp_off", methods=['POST'])
def living_room_lamp_off(): 
    control.living_room_lamp_off()

@app.route("/living_room_chairlamp_on", methods=['POST'])
def living_room_chairlamp_on():
    control.living_room_chairlamp_on()

@app.route("/living_room_chairlamp_off", methods=['POST'])
def living_room_chairlamp_off(): 
    control.living_room_chairlamp_off()

@app.route("/pc_peripherals_on", methods=['POST'])
def pc_peripherals_on():
    control.pc_peripherals_on()

@app.route("/pc_peripherals_off", methods=['POST'])
def pc_peripherals_off(): 
    control.pc_peripherals_off()        

# Kitchen
@app.route("/kitchen_lights_on", methods=['POST'])
def kitchen_lights_on():
    control.kitchen_lights_on()

@app.route("/kitchen_lights_off", methods=['POST'])
def kitchen_lights_off():
    control.kitchen_lights_off()

@app.route("/kitchen_underlights_on", methods=['POST'])
def kitchen_underlights_on():
    control.kitchen_underlights_on()

@app.route("/kitchen_underlights_off", methods=['POST'])
def kitchen_underlights_off():
    control.kitchen_underlights_off()

# Water

# Power

# Debug
@app.route("/test_switch_on", methods=['POST'])
def test_switch_on():
    control.test_switch_on()

@app.route("/test_switch_off", methods=['POST'])
def test_switch_off(): 
    control.test_switch_off()

#Web page
@app.route('/jarvis')
def jarvis():

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
    HallwayTemperature = r_server.get("Hallway Temperature")
    HallwayHumidity = r_server.get("Hallway Humidity")

    # Bathroom
    BathroomLightReading = r_server.get("Bathroom Light Reading")
    BathroomLightStatus = r_server.get("Bathroom Light Status")
    BathroomLightCommanded = r_server.get("Bathroom Light Commanded")
    BathroomTemperature = r_server.get("Bathroom Temperature")
    BathroomHumidity = r_server.get("Bathroom Humidity")
    BathroomFanStatus = r_server.get("Bathroom Fan Status")

    # Hackerspace
    HackerspaceLightStatus = r_server.get("Hackerspace Light Status")
    HackerspaceLightCommanded = r_server.get("Hackerspace Light Commanded")

    # Loft
    LoftLightReading = r_server.get("Loft Light Reading")
    LoftLightStatus = r_server.get("Loft Light Status")

    # Bedroom
    BedroomLightCommanded = r_server.get("Bedroom Light Commanded")

    # Living Room
    LivingroomLight = r_server.get("Living room Light")

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

    dict = {
# Door
    'Door - last motion':DoorMotion,
    'Door - motion count':DoorMotionCount,
    'Door - last opened':DoorOpened,
    'Door - open count':DoorOpenedCount,

# Hallway
    'Hallway Light Reading':HallwayLightReading,
    'Hallway Light':HallwayLightStatus,
    'Hallway Light Commanded':HallwayLightCommanded,
    'Hallway Bulkhead Commanded':HallwayBulkheadCommanded,
    'Hallway Temperature':HallwayTemperature,
    'Hallway Humidity':HallwayHumidity,

# Bathroom
    'Bathroom Light Reading':BathroomLightReading,
    'Bathroom Light Status':BathroomLightStatus,
    'Bathroom Light Commanded':BathroomLightCommanded,
    'Bathroom Temperature Reading':BathroomTemperature,
    'Bathroom Humidty Reading':BathroomHumidity,
    'Bathroom Fan Status':BathroomFanStatus,

# Hackerspace
    'Hackerspace Light':HackerspaceLightStatus,
    'Hackerspace Light Commanded':HackerspaceLightCommanded,

# Loft
    'Loft Light Reading':LoftLightReading,
    'Loft Light Status':LoftLightStatus,

# Bedroom
    'Bedroom Light Commanded':BedroomLightCommanded,

# Living Room
    'Living Room Light':LivingroomLight,

# Kitchen
    'Kitchen Light':KitchenLightReading,
    'Kitchen Temperature':KitchenTemperatureReading,
    'Kitchen Humidity':KitchenHumidityReading,
    'Kitchen Motion':KitchenMotionReading,

# Water
    'Hot water reading':HotWaterReading,
    'Cold water reading':ColdWaterReading,
    'Day water element reading':DayWaterElementReading,
    'Night water element reading':NightWaterElementReading,
    'Hot water':HotWaterStatus,
    'Cold water':ColdWaterStatus,
    'Day water element':DayWaterElementStatus,
    'Night water element':NightWaterElementStatus,

# Power
    'Power on CT1':Power_CT1,
    'Power on CT2':Power_CT2,
    'Power on CT3':Power_CT3,
    'Power on CT4':Power_CT4}

# Debug 
    
    return render_template('jarvis.html', result = dict)

# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)