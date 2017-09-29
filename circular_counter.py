import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

switch_input = 23

led_pins = [18, 24, 25]
led_states = [0, 0, 0]

GPIO.setup(switch_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(led_pins[2], GPIO.OUT)

led_state = False
old_input_state = True # pulled-up
count = 0

def change_led_states():
	if count == 1:
		led_states[0] = 0
		led_states[1] = 0
		led_states[2] = 1
	elif count == 2:
		led_states[0] = 0
		led_states[1] = 1
		led_states[2] = 0
	elif count == 3:
		led_states[0] = 0
		led_states[1] = 1
		led_states[2] = 1
	elif count == 4:
		led_states[0] = 1
		led_states[1] = 0
		led_states[2] = 0
	elif count == 5:
		led_states[0] = 1
		led_states[1] = 0
		led_states[2] = 1
	elif count == 6:
		led_states[0] = 1
		led_states[1] = 1
		led_states[2] = 0	
	elif count == 7:
		led_states[0] = 1
		led_states[1] = 1
		led_states[2] = 1
	else:
		led_states[0] = 0
		led_states[1] = 0
		led_states[2] = 0

while True:
	new_input_state = GPIO.input(switch_input)
	if new_input_state == False and old_input_state == True:
		count = (count + 1) % 8
		change_led_states()
	
	old_input_state = new_input_state
	GPIO.output(led_pins[0], led_states[0])
	GPIO.output(led_pins[1], led_states[1])
	GPIO.output(led_pins[2], led_states[2])
