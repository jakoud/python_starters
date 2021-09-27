def is_narcisistic(number):
    cyphers = [int(x) for x in str(number)]
    if number == sum(cypher**(len(cyphers)) for cypher in cyphers):
        return True
    else:
        return False


def main():
    for number in range(10000):
        if is_narcisistic(number) is True:
            print(number)


main()
