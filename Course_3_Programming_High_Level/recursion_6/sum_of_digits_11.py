def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)


number = int(input())
print(sum_of_digits(number))
