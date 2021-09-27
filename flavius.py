def main():
    people = int(input('podaj liczbę osób: '))
    kill = int(input('podaj odstęp: '))
    osoby = list(int(x) for x in range(1, people+1))
    pierwsza = 0
    print(osoby)
    while len(osoby) > 1:
        pierwsza = (pierwsza + kill - 1) % len(osoby)
        print('eliminujemy nr ', osoby[pierwsza])
        osoby.pop(pierwsza)
        print(osoby)


main()
