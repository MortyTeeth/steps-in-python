def print_digits(num):
    if num != 0:
        print(num % 10)
        num = num // 10
        print_digits(num)
