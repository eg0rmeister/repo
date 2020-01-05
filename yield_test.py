#!/usr/bin/python3

def foo(num):
	while True:
		num += 1
		yield num
val = foo(0)
while True:
	print(next(val))
	a = input()
	try: #if input is a number
		a = int(a)
		val = foo(a)
	except ValueError: #if input is not a number
		if a == "exit":
			exit()
