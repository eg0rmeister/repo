import serial
ser = serial.Serial("/dev/ttyACM0", timeout=1000)
while True:
	b = ser.read()
	print(b)
	try:
		ser.reset_output_buffer()
		a = '5' + ' ' + str(ord(b) * 255)
		ser.reset_input_buffer()
		ser.write(a.encode("UTF-8"))
	except TypeError:
		print("something bad happens")
