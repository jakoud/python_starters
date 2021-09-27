def main():
    login = str(input('podaj login: '))
    password = str(input('podaj hasło: '))
    baza = {'admin': 'admin', 'user': '1234', 'Josh': 'qwerty', 'b0lek': 'b0lek2000'}
    boolean = False
    for element in baza.keys():
        if login == element:
            if password == baza[login]:
                print('logowanie ok')
            else:
                print('odmowa dostępu')
        else:
            letters = list(x for x in password)
            if len(letters) > 7 and any(letter.islower() for letter in letters) and \
                                    any(letter.isupper() for letter in letters) and \
                                    any(letter.isdigit() for letter in letters):
                boolean = True
    if boolean:
        baza[login] = password
        print(baza)


main()
