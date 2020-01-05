def foo(num):
    while True:
        num += 1
        yield num
val = foo(0)
while True:
    print(next(val))
    a = input()
    try:
        a = int(a)
        val = foo(a)
    except ValueError:
        if a == "exit":
            exit()