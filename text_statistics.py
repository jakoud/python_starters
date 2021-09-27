def main():
    file = open('slowa.txt', 'r')
    lines = file.readlines()
    dict_of_appearance = {}
    for line in lines:
        line = line.strip('\n')
        if line in dict_of_appearance.keys():
            dict_of_appearance[line] += 1
        else:
            dict_of_appearance[line] = 0
    print(sorted(dict_of_appearance.items(), key=lambda x: x[1], reverse=True)[:20])
    file.close()


main()
