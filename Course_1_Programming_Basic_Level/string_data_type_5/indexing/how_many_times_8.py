string = input()

plus = 0
mult = 0


for i in range(0, len(string)):
    if string[i] == '+':
        plus += 1
    elif string[i] == '*':
        mult += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', mult, 'раз')