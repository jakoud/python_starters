def capitalize_length(lista, n):
    for iterator in range(len(lista)):
        if len(lista[iterator]) == n:
            yield lista[iterator].capitalize()


def capitalize(lista):
    for iterator in range(len(lista)):
        yield lista[iterator].capitalize()


L = ['asia', 'ala', 'ela', 'wiola', 'ola']
for element in capitalize(L):
    print(element)

print('\n')

gen = capitalize(L)
for i in range(len(L)):
    print(next(gen))

print('\n')

for element in capitalize_length(L, 3):
    print(element)
