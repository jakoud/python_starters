import numpy


def sorter(matrix, column_number):
    lista = matrix.tolist()
    return numpy.array(sorted(lista, key=lambda x: x[column_number-1]))


def main():
    lista = [[1, 7, 3], [1, 1, 5], [1, 4, 2]]
    matrix = numpy.array(lista)
    column_number = 2
    print(sorter(matrix, column_number))


main()
