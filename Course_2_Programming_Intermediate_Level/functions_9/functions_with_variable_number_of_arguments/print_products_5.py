def print_products(*args):
    d = dict()
    string = [i for i in args if type(i) == str and i != '']
    if len(string) != 0:
        for i in range(1, len(string) + 1):
            d.update({i: string[i - 1]})

        for key, value in d.items():
            print(str(key) + ') ' + value)
    else:
        print('Нет продуктов')
