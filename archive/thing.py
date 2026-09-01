import RPi.GPIO as GPIO


LED_PIN     = 22
bulkhead_light = 15
hallway_light  = 14
SWITCH_PIN    = 24


class PiThing(object):
    """Internet 'thing' that can control GPIO on a Raspberry Pi."""

    def __init__(self):
        """Initialize the 'thing'."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(bulkhead_light, GPIO.OUT)
        GPIO.setup(hallway_light, GPIO.OUT)
        GPIO.setup(SWITCH_PIN, GPIO.IN)

    def read_switch(self):
        """Read the switch state and return its current value.
        """
        return GPIO.input(SWITCH_PIN)

    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off).
        """
        GPIO.output(LED_PIN, value)

    def set_bulkhead(self, value):
        """Set the LED to the provided value (True = on, False = off).
        """
        GPIO.output(bulkhead_light, value)       
    
    def set_hallway(self, value):
        """Set the LED to the provided value (True = on, False = off).
        """
        GPIO.output(hallway_light, value)            