#!/usr/bin/python3

import serial
import paho.mqtt.client as mqtt
import time
import os

i = input()
if (i == ''):
    i = 0
    while True:
        if os.path.exists('/dev/ttyACM' + str(i)):
            i = '/dev/ttyACM' + str(i)
            break
        i += 1
print(i)


ser = serial.Serial(i, timeout=0.2)
client = mqtt.Client()
client.connect("localhost")

def on_message(client, userdata, msg):
    msg = str(msg.payload)[2:-1]
    if (msg != ''):
        ser.reset_output_buffer()
        ser.reset_input_buffer()
        print(1)
        ser.write((msg + ';').encode("utf-8"))
        print(msg)
        time.sleep(0.01)
client.on_message = on_message
client.subscribe("tst/in_ser")

#client.loop_start()
k = 0
while True:
    client.loop(0.001)
    s = ''
    i = ser.read()
    try:
        i = ord(i)
    except TypeError:
        k += 1
        print(2)
        ser.reset_output_buffer()
        ser.reset_input_buffer()
        if (k >= 7):
            ser.close()
            b = True
            while b:
                try:
                    ser.open()
                except serial.serialutil.SerialException:
                    continue
                else:
                    b = False
            time.sleep(2)

        continue
    if (chr(i) == ':'):
        k = 0
        while True:
            try:
                i = ord(ser.read())
            except TypeError:
                k += 1
                if (k >= 100):
                    ser.close()
                    ser.open()
                    time.sleep(2)
                continue
            except serial.serialutil.SerialException:
                try:
                    ser.open()
                except serial.serialutil.SerialException:
                    continue
                k = 0
            k = 0
            if (chr(i) == ';'):
                break
            if (chr(i) == '.'):
                s += '.'
            else:
                s += str(i)
        client.publish("tst/out_ser", s)
        #print(s)
    ser.reset_output_buffer()
    ser.reset_input_buffer()
