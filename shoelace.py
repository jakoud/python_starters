def shoelace(*tuples):
    list_x, list_y = [], []
    suma = 0
    for tup in tuples:
        list_x.append(tup[0]), list_y.append(tup[1])
    for iterator in range(len(list_x)-1):
        suma += list_x[iterator]*list_y[iterator+1]
    suma += list_x[len(list_x)-1]*list_y[0]
    for iterator in range(len(list_x) - 1):
        suma -= list_x[iterator+1]*list_y[iterator]
    suma -= list_x[0]*list_y[len(list_x)-1]
    return suma/2


print(shoelace((0, 0), (4, 0), (0, 3)))
print(shoelace((0, 0), (1, 0), (1, 1), (0, 1)))
