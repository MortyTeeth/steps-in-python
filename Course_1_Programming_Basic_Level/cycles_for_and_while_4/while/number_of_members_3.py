word = input()
n = 0
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    n = n + 1
    word = input()
print(n)