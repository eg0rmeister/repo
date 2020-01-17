#!/usr/bin/python3
#!C:\\Users\\karpu\\AppData\\Local\\Programs\\Python\\Python38


import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("localhost")
while True:
    i = input("topic(spacebar)message:\n").split()
    try:
        client.publish(i[0], i[1])
    except IndexError:
        continue
