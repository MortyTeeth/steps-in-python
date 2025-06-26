from string import *

with (open('nums.txt', 'r', encoding='utf-8')) as file:
    after_change = []
    sum = 0
    for line in file:
        string = ''
        for symbol in line:
            if symbol not in str(ascii_lowercase + '\n'):
                string += symbol
            else:
                string += symbol.replace(symbol, ' ')
        for k in string.split():
            sum += int(k)
    print(sum)
