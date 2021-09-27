import sympy
import random
import math

x = sympy.Symbol('x')


def taylor(function, x0, n):
    return function.series(x, x0, n).removeO()


#print(taylor(sympy.sin(x), 0, 4).subs(x, 1))
list_of_faults = []

for element in range(1, 10):
    threshold = 8
    difference = random.random()
    if taylor(sympy.log(x), element + difference, threshold) != 0:
        list_of_faults.append(
            (int(math.log(element) - taylor(sympy.log(x), element + difference, threshold).subs(x, element)),
             taylor(sympy.log(x), element + difference, threshold).subs(x, element), element, difference))
        #print(element, math.log(element), taylor(sympy.log(x), element + difference, threshold).subs(x, element),
        #      threshold, difference)
        #print(taylor(sympy.log(x), element + difference, threshold))


lista = sorted(list_of_faults, key=lambda tup: tup[0], reverse=True)[0:10]
for element in lista:
    print(element)
