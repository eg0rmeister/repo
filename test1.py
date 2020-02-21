import serial
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost")
def on_message(client, userdata, msg):
	#print(msg.payload)
	msg = str(msg.payload)[2:-1]
	print('\t\t', msg)
	ser.write(msg.encode("UTF-8"))
client.on_message = on_message
client.subscribe("tst/in_ser")

ser = serial.Serial("/dev/ttyACM0", timeout=1)
while True:
	if ser.in_waiting > 0:
		client.loop(0.01)
		b = ser.readline()[:-1]
		#print("hello, ", b)
		try:
			a = '5' + ' ' + str(b[0])
		except IndexError:
			print("bad")
		else:
			print(b, a)
			ser.reset_input_buffer()
			ser.reset_output_buffer()
			client.publish("tst/out_ser", a)
