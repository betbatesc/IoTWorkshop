import RPi.GPIO as GPIO
led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# Set frequency to 500 Hz
pwm_led = GPIO.PWM(led_pin, 500)

# Set duty cycle to 100
pwm_led.start(100)

while True:
	duty = int(input("Enter Brightness (0 to 100):"))
	if duty < 100:
		pwm_led.ChangeDutyCycle(duty)
