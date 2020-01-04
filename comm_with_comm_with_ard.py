#!C:\\Users\\karpu\\AppData\\Local\\Programs\\Python\\Python38

import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("localhost")
def on_message(clients, userdata, msg):
    msg = str(msg.payload)[2:-1]
    if (msg != ''):
        client.publish("tst/in_ser", '5' + '.' + msg.split('.')[0], qos=1)
        client.publish("tst/in_ser", '6' + '.' + msg.split('.')[1], qos=1)
        print(msg)
client.on_message = on_message
client.subscribe("tst/out_ser")
client.loop_forever()
