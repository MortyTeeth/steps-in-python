def secret_word(line_with_symbols, num_symbols):
    first_dict = {}
    s_s = ':'
    second_dict = {}
    third_dict = {}
    for i in range(num_symbols):
        line = input()
        line_after_edit = ''
        for k in range(len(line)):
            if line[k] != s_s:
                line_after_edit += line[k]
        first_dict.update({line_after_edit[0]: int(line_after_edit[2])})

    for symbol in line_with_symbols:
        if symbol not in second_dict:
            second_dict[symbol] = 1
        else:
            second_dict[symbol] += 1

    dict_first = dict(zip(first_dict.values(), first_dict.keys()))

    dict_second = dict(zip(second_dict.values(), second_dict.keys()))

    for l in range(len(line_with_symbols)):
        for key, value in dict_second.items():
            if line_with_symbols[l] == value:
                print(dict_first[key], end='')


line_with_symbols = input()
num_symbols = int(input())

secret_word(line_with_symbols, num_symbols)
