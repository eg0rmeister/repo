#!/usr/bin/python3

def foo(num):
    k = num
    while True:
        num += 1
        print(str(k) + " is now " + str(num))
        yield num
val = [foo(0)]
while True:
    for i in val:
        print(next(i))
    a = input("input:")
    try:
        a = int(a)
        val.append(foo(a))
    except ValueError:
        if a == "exit":
            exit()
