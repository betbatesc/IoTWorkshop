import RPi.GPIO as GPIO
import time

# set board mode to Broadcom
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT)

print("LED on")

GPIO.output(18, GPIO.HIGH)

time.sleep(5)

print("LED off")

GPIO.output(18, GPIO.LOW)
