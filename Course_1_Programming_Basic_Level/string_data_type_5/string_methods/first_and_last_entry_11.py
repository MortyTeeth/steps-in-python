string = input()

count = 0

if string.count('f') == 1:
    print(string.find('f'))
elif string.count('f') > 1:
    print(string.find('f'), string.rfind('f'))
else:
    print('NO')