import serial
ser = serial.Serial("/dev/ttyACM0")
while True:
	a = ser.readline().decode("UTF-8")
	print(a)
