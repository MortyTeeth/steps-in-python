b = 0

for i in range(10):
    a = int(input())
    if a % 2 == 0:
        b = b + 1
if b == 10:
    print('YES')
else:
    print('NO')