import numpy
import random


def randomizer():
    lista = []
    for iterator in range(3):
        lista.append([])
    for element in lista:
        for iterator in range(3):
            element.append(random.randint(-9, 9))
    M = numpy.array(lista)
    return numpy.linalg.det(M)


def main():
    suma = 0
    zero_determinant = 0
    for iterator in range(1000):
        add = randomizer()
        if add == 0:
            zero_determinant += 1
        suma += add
    estimated_determinant = suma/1000
    frequency_zero_determinant = zero_determinant/1000
    print(estimated_determinant)
    print(frequency_zero_determinant)


main()
