import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)          # Read output from PIR motion sensor
GPIO.setup(18, GPIO.OUT)        # LED output pin

while True:
    input = GPIO.input(5)
    if input == 0:
        print("No intruders ", input)
        GPIO.output(18, GPIO.LOW)  # Turn Off led
        time.sleep(0.1)
    else:
        print("Intruder detected: ", input)
        GPIO.output(18, GPIO.HIGH)  # Turn On led
        time.sleep(0.1)