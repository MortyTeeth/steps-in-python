def get_next_prime(num):
    list_with_nums = [k for k in range(1, num + num)]
    list_with_primes = [2, 3]
    for k in list_with_nums:
        counter = 0
        for l in list_with_nums:
            if k % l == 0 and k % 2 != 0 and k % 3 != 0:
                counter += 1
        if counter == 2:
            list_with_primes.append(k)

    for s in list_with_primes:
        if num < s:
            return s


n = int(input())

print(get_next_prime(n))
