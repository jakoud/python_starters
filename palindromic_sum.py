def reverser(number):
    reverse = 0
    cond = len(str(number))

    while number > 0:
        reverse = reverse*10 + number % 10
        number = number // 10

    if len(str(reverse)) < cond:
        for iterator in range(cond-len(str(reverse))):
            str_reverse = '0' + str(reverse)
        return str_reverse

    return reverse


def is_palindrome(number):
    digits = list(int(x) for x in str(number))
    iterator = 0
    while iterator < len(digits)/2 + 1:
        if digits[iterator] != digits[len(digits)-iterator-1]:
            return False
        iterator += 1
    return True


def main():
    number = int(input('podaj liczbę: '))
    suma = number + int(reverser(number))
    while is_palindrome(suma) is False:
        print(number, '+', reverser(number), '=', suma)
        print('próbuję dalej...')
        number = suma
        suma = suma + int(reverser(suma))

    print(number, '+', reverser(number), '=', suma)
    print('koniec!')


main()
