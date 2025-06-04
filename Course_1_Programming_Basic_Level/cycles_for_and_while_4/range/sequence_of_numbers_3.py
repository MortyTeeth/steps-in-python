m = int(input())
n = int(input())

if m - n == 1 and m % 2 == 0:
    print(n)
elif m - n == 1 and m % 2 == 1:
    print(m)

elif m > n and m % 2 == 0:
    for i in range(m - 1, n, -2):
        print(i)
elif m > n and m % 2 == 1:
    for i in range(m, n, -2):
        print(i)