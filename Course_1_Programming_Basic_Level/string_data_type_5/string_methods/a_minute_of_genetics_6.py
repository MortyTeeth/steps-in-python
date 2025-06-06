string = input()

A = string.count('а') + string.count('А')
G = string.count('г') + string.count('Г')
C = string.count('ц') + string.count('Ц')
T = string.count('т') + string.count('Т')

print('Аденин:', A)
print('Гуанин:', G)
print('Цитозин:', C)
print('Тимин:', T)