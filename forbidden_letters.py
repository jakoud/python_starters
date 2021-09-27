def main():
    forbidden_str = input('zakazane literki: ')
    forbidden_list = list(x for x in forbidden_str)
    string = str(input('tekst: '))
    for letter in forbidden_list:
        string = string.replace("{letter}".format(letter=letter.upper()), "")
        string = string.replace("{letter}".format(letter=letter.lower()), "")
    string = string.replace(" ", "")
    print('wynik: ', string)


main()
