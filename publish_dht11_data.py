#!/usr/bin/python
import sys
import Adafruit_DHT    
import paho.mqtt.client as mqtt
import time

sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor

data_pin = 4
broker_address = "192.168.0.101"

client = mqtt.Client("mRaspPiIoTWorkshopAGT")
client.connect(broker_address)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, data_pin)
    
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        client.publish("agt/dht11/temperature", "{0:0.1f}".format(temperature))
        client.publish("agt/dht11/humidity", "{0:0.1f}".format(humidity))    
        time.sleep(5)
    else:
        print('Failed to get reading. Try again!')
