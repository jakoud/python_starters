def approval(set1, set2, counter):
    if set1 == set2:
        print('dobrze')
        counter += 1
    else:
        print('źle')

    return counter


def main():
    set1 = set(str(input('podaj zbiór A: ')).split())
    set2 = set(str(input('podaj zbiór B: ')).split())
    counter = 0

    suma = set(str(input('podaj sumę zbiorów: ')).split())
    counter = approval(suma, set1.union(set2), counter)

    przeciecie = set(str(input('podaj przecięcie zbiorów: ')).split())
    counter = approval(przeciecie, set1.intersection(set2), counter)

    roznica1 = set(str(input('podaj różnicę A\B: ')).split())
    counter = approval(roznica1, set1.difference(set2), counter)

    roznica2 = set(str(input('podaj różnicę B\A: ')).split())
    counter = approval(roznica2, set2.difference(set1), counter)

    symmetric_dif = set(str(input('podaj różnicę symetryczną: ')).split())
    counter = approval(symmetric_dif, set1.symmetric_difference(set2), counter)

    print(str(counter)+'/5')


main()
