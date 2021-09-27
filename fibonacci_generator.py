def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fib()
for i in fib:
    print(i)
    if len(str(i)) == 3:
        fib.close()
