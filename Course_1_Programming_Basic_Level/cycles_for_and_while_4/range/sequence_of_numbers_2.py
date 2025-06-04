import math

m = int(input())
n = int(input())

if (m < n) and m < 0:
    for i in range(n + abs(m) + 1):
        print(m + i)
elif (m > n) and n < 0:
    for i in range(m, n - 1, -1):
        print(i)
elif m < n:
    for i in range(n):
        print(m + i)
elif m > n:
    for i in range(m):
        print(m - i)
else:
    print(m)