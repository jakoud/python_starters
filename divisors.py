import math


def divisors(number):
    integer = 1
    list_of_divisors = []
    while integer < math.sqrt(number)+1:
        if number % integer == 0:
            list_of_divisors.append(integer)
            list_of_divisors.append(int(number/integer))
        integer += 1
    return sorted(list(dict.fromkeys(list_of_divisors)))


#print(divisors(12))
