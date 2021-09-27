from divisors import divisors


def polynomial(coefficient_list, number):
    suma = 0
    for iterator in range(len(coefficient_list)):
        suma += coefficient_list[iterator]*number**(len(coefficient_list)-1-iterator)
    return suma


def rational_roots(*coefficients):
    coefficients_list = list(coefficients)
    divisors_max = divisors(abs(coefficients_list[0]))
    divisors_min = divisors(abs(coefficients_list[len(coefficients_list)-1]))
    all_divisors = []
    for max_div in divisors_max:
        for min_div in divisors_min:
            all_divisors.append(min_div/max_div)
            all_divisors.append(-min_div/max_div)

    all_divisors = sorted(list(dict.fromkeys(all_divisors)))
    rational_roots_list = []
    for divisor in all_divisors:
        if polynomial(coefficients_list, divisor) == 0:
            rational_roots_list.append(divisor)

    print(sorted(list(dict.fromkeys(rational_roots_list))))


rational_roots(4, -12, 5, 8, -3, -2)
rational_roots(1, 2, 1)
rational_roots(1, 2, 3)
