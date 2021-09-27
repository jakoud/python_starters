import random


def cows(code, guess):
    counter = 0
    for iterator in range(len(guess)):
        if guess[iterator] in code and guess[iterator] != code[iterator]:
            counter += 1
    return counter


def bulls(code, guess):
    counter = 0
    for iterator in range(len(guess)):
        if guess[iterator] == code[iterator]:
            counter += 1
    return counter


def guess_int():
    guess = [int(letter) for letter in input('guess the code: ')]
    return guess


def code_rand():
    code = []
    while len(code) < 4:
        rand = random.randint(0, 9)
        if rand not in code:
            code.append(rand)
    return code


def main():
    guess = guess_int()
    counter = 1
    code = code_rand()
    while guess != code:
        print('Cows: '+str(cows(code, guess)))
        print('Bulls: '+str(bulls(code, guess)))
        guess = guess_int()
        counter += 1
    print('Amount of tries: '+str(counter))


main()
