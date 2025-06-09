from string import *


def dolina(n_s):
    for i in range(1, n_s + 1):
        line = input()
        newline = ''
        for symbol in line:
            if symbol in 'anton':
                newline += symbol

        new_new_line = ''
        if 'a' in newline:
            new_new_line += 'a'
            newline = newline[newline.find('a'):]
        if 'n' in newline:
            new_new_line += 'n'
            newline = newline[newline.find('n'):]
        if 't' in newline:
            new_new_line += 't'
            newline = newline[newline.find('t'):]
        if 'o' in newline:
            new_new_line += 'o'
            newline = newline[newline.find('o'):]
        if 'n' in newline:
            new_new_line += 'n'
            newline = newline[newline.find('n'):]
        if new_new_line == 'anton':
            print(i, end=' ')


num_str = int(input())
dolina(num_str)