import jarvis_control
import time


# Create the pi thing.
jarvis_control = jarvis_control.jarvis_control()

# Now loop forever blinking the LED.
print('Looping with socket turning on and off (Ctrl-C to quit)...')
while True:
    print('on')
    jarvis_control.bathroom_light_on()
    time.sleep(1)
    print('off')
    jarvis_control.bathroom_light_off()
    time.sleep(1)