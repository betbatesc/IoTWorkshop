import paho.mqtt.client as mqtt

broker_address = "192.168.0.101"

client = mqtt.Client("mRaspPiIoTWorkshop")
client.connect(broker_address)
client.publish("girlfriend/horny", "YES")
