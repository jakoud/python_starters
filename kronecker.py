import numpy


def kronecker(matrix1, matrix2):
    lista1 = matrix1.tolist()
    lista2 = matrix2.tolist()
    wynikowa = []
    operacyjna = []
    for element in lista1:
        for element2 in lista2:
            for coefficient in element:
                for coefficient2 in element2:
                    operacyjna.append(coefficient*coefficient2)
            wynikowa.append(operacyjna)
            operacyjna = []
    return numpy.array(wynikowa)


def main():
    matrix1 = numpy.array([[1,2], [2,3]])
    matrix2 = numpy.array([[1,3,5], [1,2,3]])
    print(kronecker(matrix1, matrix2))
    print(numpy.kron(matrix1, matrix2))


main()
