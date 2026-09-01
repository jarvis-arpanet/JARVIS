import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

while (1):
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	time.sleep(3)
	GPIO.output(14, 1)
	GPIO.output(15, 0)
	time.sleep(3)