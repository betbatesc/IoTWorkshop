from tkinter import *
import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 500)
pwm.start(100)

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.update)
		scale.grid(row=0)
		
	def update(self, duty):
		pwm.ChangeDutyCycle(float(duty))

root = Tk()
root.wm_title('PWM')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
