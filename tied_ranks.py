def tied_ranks(vector):
    returned = vector
    for element in set(vector):
        iterator = 0
        rank = 0
        occurence = 0

        while iterator < len(vector):
            if vector[iterator] == element:
                rank += iterator+1
                occurence += 1
            iterator += 1

        for n in range(iterator):
            if vector[n] == element:
                returned[n] = rank/occurence

    return returned


print(tied_ranks([1,2,2,8]))
print(tied_ranks([1,2,2,2,8]))