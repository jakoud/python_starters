import random


def main():
    dict_of_outcomes = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for iterator in range(100):
        dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
        dict_of_outcomes[dice1+dice2] += 1
    for key in dict_of_outcomes.keys():
        return_str = ''
        for iterator in range(dict_of_outcomes[key]):
            return_str += '*'
        print(str(key)+'\t'+return_str)


main()
