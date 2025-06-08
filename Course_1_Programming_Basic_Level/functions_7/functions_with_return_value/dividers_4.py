def number_of_factors(num):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
    pass


n = int(input())

print(number_of_factors(n))