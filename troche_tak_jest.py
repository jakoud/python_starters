import random


def generator():
    boolean = random.randint(0, 1)
    if boolean == 1:
        print('Trochę tak jest.')
    else:
        print('Doskonale.')


print('Generator Tomaszewskiego. Jeżeli chcesz zakończyć, wpisz "koniec".')
zdanie = input('Podaj zdanie: ')
while zdanie != 'koniec':
    generator()
    zdanie = input('Podaj kolejne zdanie: ')
