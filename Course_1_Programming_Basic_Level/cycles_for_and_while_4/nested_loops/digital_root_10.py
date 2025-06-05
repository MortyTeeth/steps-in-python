def digital_root(n):
    while n > 9:
        n = n % 10 + n // 10
    print(n)


num = int(input())

digital_root(num)