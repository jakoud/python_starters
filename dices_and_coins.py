import random


def the_round(guess, coins):
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    if guess == dice1 + dice2:
        coins += guess
    else:
        coins -= 1
    return coins


def the_game(rounds):
    player_coins, computer_coins = rounds, rounds
    for iterator in range(rounds):
        player_guess = int(input('guess the sum: '))
        computer_guess = random.randint(2, 12)
        player_coins = the_round(player_guess, player_coins)
        computer_coins = the_round(computer_guess, computer_coins)

    if computer_coins > player_coins:
        print('computer wins')
    else:
        print('player wins')


the_game(1)
