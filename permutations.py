def permutations(lista):
    if len(lista) < 2:
        return lista

    list_permutations = []

    for i in range(len(lista)):
        m = lista[i]
        remaining = lista[:i] + lista[i + 1:]

        for p in permutations(remaining):
            list_permutations.append(str(m) + str(p))

    return list_permutations


print(permutations([1, 2, 3]))
