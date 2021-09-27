import numpy
import random


def fill_in():
    lista = []
    for iterator in range(10):
        lista.append([])
    for element in lista:
        for iterator in range(10):
            element.append(random.randint(-10, 10))
    return numpy.array(lista)


def replacer(M):
    for row in range(10):
        for column in range(10):
            if M[row, column] < 0:
                M[row, column] = 0
    for row in range(10):
        for column in range(10):
            if M[row, column] % 2 == 1:
                M[row, column] *= 2
    return M


def occurence(M):
    lista = []
    for row in range(10):
        for column in range(10):
            lista.append(M[row, column])
    dict_of_occurence = {}
    for element in set(lista):
        occurence = 0
        for row in range(10):
            for column in range(10):
                if M[row, column] == element:
                    occurence += 1
        dict_of_occurence[element] = occurence
    return dict_of_occurence


def main():
    M = fill_in()
    M = replacer(M)
    dict_of_occurence = occurence(M)
    print(sorted(dict_of_occurence.items(), key=lambda x: x[1], reverse=True)[0])


main()
