import serial
ser = serial.Serial("/dev/ttyACM0", timeout=1)
while True:
	if ser.in_waiting > 0:
		b = ser.readline()
		print(b)
		try:
			a = '5' + ' ' + str(int(b[:-1])*255)
			ser.reset_input_buffer()
			ser.reset_output_buffer()
			ser.write(a.encode("UTF-8"))
		except ValueError:
			print("bad")
