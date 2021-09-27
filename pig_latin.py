def main():
    with open('pig.txt', 'r') as file:
        output_file = open('pig_latin.txt', 'w')
        vowels = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
        for line in file.readlines():
            words = [word for word in line.split()]
            return_string = ''
            for word in words:
                if word[0] not in vowels and word[1] in vowels:
                    return_string += '{value}ay '.format(value=(word[1:]+word[0]).lower())
                elif word[0] not in vowels and word[1] not in vowels:
                    return_string += '{value}ay '.format(value=(word[2:]+word[:2]).lower())
                else:
                    return_string += '{value}way '.format(value=word.lower())
            output_file.write(return_string+'\n')


main()
