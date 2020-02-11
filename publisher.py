import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("127.0.0.1")
while True:
    i = input("topic(spacebar)message:\n").split()
    try:
        client.publish(i[0], i[1])
    except IndexError:
        continue

