import jarvis_control_2
import time


# Create the pi thing.
control = jarvis_control_2.jarvis_control_2()

# Now loop forever blinking the LED.
print('Looping test code (Ctrl-C to quit)...')
while True:
	print('on')
	control.bathroom_fan_on()
	time.sleep(30)
	#rint('off')
	#control.hallway_light_on()
	#time.sleep(3)