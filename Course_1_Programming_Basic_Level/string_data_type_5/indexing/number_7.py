string = input()

count = 0

for i in range(0, len(string)):
    if string[i] in '1234567890':
        count += 1
        break
    else:
        count = 0
if count == 0:
    print('Цифр нет')
else:
    print('Цифра')