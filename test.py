import serial
import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("localhost")

def on_message(client, userdata, msg):
	msg = str(msg.payload())[2:-1]
	ser.write((msg.split('.')[0] + msg.split('.')[1] + ' ' + '1000').encode("UTF-8"))

client.subscribe("tst/in_ser")
client.on_message = on_message


ser = serial.Serial("/dev/ttyACM0", timeout=0.1)
while True:
	print(1)
	print(2)
	a = ser.read()
	print(3)
	client.loop(0.1)
	if str(a) != "b''":
		print(ord(a))
		if ord(a) == 254:
			ser.timeout = 5
			a = chr(ord(ser.read()))
			print(ord(a))
			while(a != 255):
				a += chr(ord(ser.read()))
				print(a)
			client.publish(a)
			ser.timeout = 0.1
	else:
		print("bad")
	client.loop(1)
	print(ser.read())
	ser.reset_input_buffer()
	ser.reset_output_buffer()
