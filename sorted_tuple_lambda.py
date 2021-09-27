L = [('Johnny', 17, 91), ('Bony', 17, 99), ('John', 17, 99), ('Tom', 19, 80), ('Jason', 19, 85)]
print(sorted(L, key=lambda t: (t[1], t[2], t[0])))
