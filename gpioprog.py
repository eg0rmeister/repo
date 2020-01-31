import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(8, gpio.OUT)
while True:
	gpio.output(8, True)
	
