def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0 and num != 0:
            count += 1
        else:
            count = count
    if count == 2:
        return True
    else:
        return False
    pass


n = int(input())

print(is_prime(n))