def get_factors(num):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l
    pass


n = int(input())

print(get_factors(n))