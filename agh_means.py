def arithmetic_mean(lista):
    sum_total = 0
    for element in lista:
        sum_total += element
    return sum_total/len(lista)


def geometric_mean(lista):
    factor = 1
    for element in lista:
        factor *= element
    return factor**(1/len(lista))


def harmonic_mean(lista):
    sum_inverts = 0
    for element in lista:
        sum_inverts += 1/element
    return len(lista)/sum_inverts


def main():
    mean_type = str(input('choose mean type (a, g, h): ')).lower()
    list_of_values = []
    numbers_amount = int(input('how many numbers?: '))
    for iterator in range(numbers_amount):
        list_of_values.append(int(input('give me {ith} number: '.format(ith=iterator+1))))
    if mean_type == 'a':
        print(arithmetic_mean(list_of_values))
    elif mean_type == 'g':
        print(geometric_mean(list_of_values))
    else:
        print(harmonic_mean(list_of_values))


main()
