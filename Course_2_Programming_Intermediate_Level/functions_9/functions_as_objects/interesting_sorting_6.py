numbers = input().split()


def sum_of_digits(number):
    # Возвращаем сумму цифр числа
    return sum(int(digit) for digit in number)


# Сортируем числа по сумме их цифр
sorted_numbers = sorted(numbers, key=sum_of_digits)

# Выводим исходные числа, отсортированные по сумме их цифр
print(*sorted_numbers)
