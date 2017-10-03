import RPi.GPIO as GPIO
import time
import smtplib

GMAIL_USER = 'betbatesc@gmail.com'
GMAIL_PASS = 'Agt1992-2035'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)          # Read output from PIR motion sensor
GPIO.setup(18, GPIO.OUT)        # LED output pin

def send_email(recipient, subject, text):
	smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	smtp_server.ehlo()
	smtp_server.starttls()
	# smtp_server.ehlo
	smtp_server.login(GMAIL_USER, GMAIL_PASS)
	header = 'To: ' + recipient + '\n' + 'From: ' + GMAIL_USER
	header += '\n' + 'Subject: ' + subject + '\n'
	msg = header + '\n' + text + '\n\n'
	smtp_server.sendmail(GMAIL_USER, recipient, msg)
	smtp_server.close()

while True:
    input = GPIO.input(5)
    if input == 0:
        print("No intruders ", input)
        GPIO.output(18, GPIO.LOW)  # Turn Off led
        time.sleep(5)
    else:
        print("Intruder detected: ", input)
        GPIO.output(18, GPIO.HIGH)  # Turn On led
        time.sleep(5)
        send_email('streetball1992@hotmail.com', 'Alert', 'Somebody has broken in your house :O')
        







