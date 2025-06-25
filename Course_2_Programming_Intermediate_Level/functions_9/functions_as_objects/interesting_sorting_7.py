numbers = input().split()


def sum_of_digits(number):
    # Возвращает сумму цифр числа
    return sum(int(digit) for digit in number)


def sorting_key(number):
    # Возвращает кортеж (сумма цифр, само число как целое)
    return (sum_of_digits(number), int(number))


# Сортируем числа с использованием функции sorting_key
sorted_numbers = sorted(numbers, key=sorting_key)

# Выводим числа в нужном порядке
print(*sorted_numbers)
