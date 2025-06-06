string = input()

flag = False

for i in range(0, len(string)):
    if string[:] == string[::-1]:
        flag = True
    else:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')