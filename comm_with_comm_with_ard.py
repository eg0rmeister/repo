#!/usr/bin/python3

import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("localhost")
def on_message(clients, userdata, msg):
	msg = str(msg.payload)[2:-1]
	if (msg != ''):
		msg = msg.split('.')
		if(msg[0] == '255'):
			msg[1] = '255'
			msg[0] = '0'
		elif (msg[1] == '255'):
			msg[1] = '0'
			msg[0] = '255'
		else:
			msg[0] = '120'
			msg[1] = '120'
		client.publish("tst/in_ser", '5' + '.' + msg[0], qos=1)
		client.publish("tst/in_ser", '6' + '.' + msg[1], qos=1)
		print(msg)
client.on_message = on_message
client.subscribe("tst/out_ser")
client.loop_forever()
