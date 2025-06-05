a = int(input())

num = 1

for row in range(1, 1 + a):
    for col in range(1, row + 1):
        print(num, end=' ')
        num = num + 1
    print()