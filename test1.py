import serial
ser = serial.Serial("/dev/ttyACM0", timeout=1)
while True:
 if ser.in_waiting > 0:
  b = ser.readline()
  print(b)
  ser.reset_output_buffer()
  ser.reset_input_buffer()
  a = b.split()
  print(a)
  for i in range(len(a)):
   a[i] = int(a[i])
  print('a =', a)
  print(b)
