def palindromes():
    while True:
        for i in range(1, 100000000):
            if str(i) == str(i)[::-1]:
                yield i
