a = int(input())

b = a // 100
c = a // 10 % 10
d = a % 10

if (max(b, c, d) - min(b, c, d)) == ((b + c + d) - max(b, c, d) - min(b, c, d)):
    print('Число интересное')
else:
    print('Число неинтересное')