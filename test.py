import serial
ser = serial.Serial("/dev/ttyACM0", timeout=1000)
while True:
 ser.reset_output_buffer()
 b = ser.readline()
 if (chr(b[0]) == ':'):
  ser.reset_input_buffer()
  print (b)
  b = b.split()
  b[0] = int(b[0][1:])
  b[1] = int(b[1])
  ser.write((str(b[0] + 3) + ' ' + str(b[1]//4)).encode("UTF-8"))
  print ("b[0] = " + str(b[0]))
  print ("b[1] = " + str(b[1]))
 else:
  print("bad")
