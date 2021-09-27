def main():
    base_file = open('dane.txt', 'r')
    output_file = open('dane_uporzadkowane.txt', 'w')
    lines = base_file.readlines()
    for line in lines:
        list_of_values = [value for value in line.split(',')]
        return_string = ''

        for value in list_of_values:
            value = value.replace('\n', '')
            if value == '':
                return_string += '0 '
            else:
                return_string += '{value} '.format(value=value)

        output_file.write(return_string+'\n')

    base_file.close()
    output_file.close()


main()
