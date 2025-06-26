def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        keys = [i for i in file.readline().split(',')]
        main_list = []
        for line in file:
            string = [str(i) for i in line.split(',')]
            dictionary = {}
            for i in range(len(keys)):
                dictionary.update({keys[i].rstrip(): string[i].rstrip()})
            main_list.append(dictionary)
        return main_list
