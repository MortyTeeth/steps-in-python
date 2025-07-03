def number_of_digits(number):
    if number < 10:
        return 1
    else:
        return 1 + number_of_digits(number // 10)


num = int(input())
print(number_of_digits(num))
