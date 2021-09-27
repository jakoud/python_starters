import random


def bootstrap():
    data = [4, 7, 2, 4, 8, 3, 2]
    means = []
    for iterator in range(100):
        suma = 0
        for choice in range(7):
            suma += random.choice(data)
        means.append(suma/7)

    print(sorted(means)[5], sorted(means)[94])


bootstrap()
