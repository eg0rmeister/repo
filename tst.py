import serial



ser = serial.Serial("/dev/ttyACM0")
while True:
	print(ser.read())
