x = int(input())

if ((x >= 1000) and (x <= 9999)) and ((x % 7 == 0) or (x % 17 == 0)):
    print('YES')
else:
    print('NO')