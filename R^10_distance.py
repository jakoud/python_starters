import numpy
import random
import math


def distance(vector1, vector2):
    suma = 0
    for i in range(len(vector1)):
        suma += (vector1[i]-vector2[i])**2
    return math.sqrt(suma)


def main():
    lista = []
    for iterator in range(10):
        lista.append([])
    for element in lista:
        for iterator in range(100):
            element.append(random.randint(-10, 10))
    matrix = numpy.array(lista)

    for iterator in range(100):
        element = matrix[:, iterator]
        for iterator2 in range(100):
            print(distance(element, matrix[:, iterator2]))


main()
