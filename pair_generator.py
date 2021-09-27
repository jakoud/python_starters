n = 4
L1 = list((i, j) for i in range(1, n) for j in range(1, n))
L2 = list((i, j) for i in range(1, n) for j in range(1, n) if i < j)
L3 = list((i, j) for i in range(0, n) for j in range(i+1, i**2))
print(L1)
print(L2)
print(L3)
