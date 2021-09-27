import functools


L = [i for i in range(100)]
L1 = list(filter(lambda x: x % 8, L))
L2 = list(map(lambda x: x**3, L1))
value = functools.reduce(lambda x, y: x+y, L2)/len(L2)

print(value)
