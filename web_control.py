from bottle import route, run
import RPi.GPIO as GPIO

host = '192.168.0.125'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pins = [18, 24, 25]
led_states = [0, 0, 0]

GPIO.setup(led_pins[0], GPIO.OUT)
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(led_pins[2], GPIO.OUT)
		
def html_for_led(led):
	l = str(led)	
	result = "<input type='button' onclick='changed(" + l + ")'"
	result += " value='LED " + l + "'/>"
	return result

def update_leds():
	for i, value in enumerate(led_states):
		GPIO.output(led_pins[i], value)
		
@route('/')
@route('/<led>')
def index(led = "n"):
	if led != "n":
		led_num = int(led)
		led_states[led_num] = not led_states[led_num]
		update_leds()
	response = "<html>"
	response += "<body>"
	response += "<style>h1 {color:red;} body {background-color:DodgerBlue;}</style>"
	response += "<script>"
	response += "function changed(led)"
	response += "{"
	response += " window.location.href='/' + led"
	response += "}"
	response += "</script>"
	
	response += "<h1>GPIO Control</h1>"
	response += "<h2>LEDs</h2>"
	response += html_for_led(0)
	response += html_for_led(1)
	response += html_for_led(2)
	response += "</body></html>"
	return response
			
run(host = host, port = 80)		
		
