import paho.mqtt.client as mqtt
client = mqtt.Client()
def on_message(client, userdata, msg):
	print(msg.payload)
client.on_message = on_message
client.connect("localhost")
client.subscribe("tst/tst")
client.loop_forever()
