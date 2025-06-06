string = input()

gl = 0
sogl = 0

for i in range(0, len(string)):
    if string[i] in 'АОУЫЭЕЁИЮЯ' or string[i] in 'аоуыэеёиюя':
        gl += 1
    if string[i] in 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ' or string[i] in 'бвгджзйклмнпрстфхцчшщ':
        sogl += 1
print('Количество гласных букв равно', gl)
print('Количество согласных букв равно', sogl)