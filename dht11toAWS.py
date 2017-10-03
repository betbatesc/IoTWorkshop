#!/usr/bin/python
import sys
import Adafruit_DHT
import os
import sys
import AWSIoTPythonSDK
sys.path.insert(0, os.path.dirname(AWSIoTPythonSDK.__file__))
# Now the import statement should work
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import argparse

# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")

args = parser.parse_args()
host = args.host
rootCAPath = args.rootCAPath
certificatePath = args.certificatePath
privateKeyPath = args.privateKeyPath

sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
pin = 4

# Sensor Serial Number
sensor_sn = 'dev_r00000001'

# Topic
topic = 'myrpi/' + sensor_sn

# Custom Callback
def customCallback(client, userdata, message):
	print('Received a new message: ')
	print(message.payload)
	print('from topic: ')
	print(message.topic)
	print('--------------\n\n')

myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub")
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

while True:
	try:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
		if humidity is not None and temperature is not None:
			print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
			#msg = '"Device": "{:s}", "Temperature": "{0:0.1f}*C", "Humidity": "{1:0.1f}%"'.format('DHT11', temperature, humidity)
			msg = 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
			msg = '{' + msg + '}'
			myAWSIoTMQTTClient.publish(topic, msg, 1)        
		else:
			print('Failed to get reading. Try again!')
	except KeyboardInterrupt:
		pass
	
print('Exiting the loop')
myAWSIoTMQTTClient.disconnect()
print('Disconnected from AWS')

