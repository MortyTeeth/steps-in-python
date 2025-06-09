def product_of_numbers(numbers):
    list_with_numbers = []
    for i in range(numbers):
        num_int = int(input())
        list_with_numbers.append(num_int)

    result = int(input())

    counter = 0

    for i in range(len(list_with_numbers)):
        for k in range(i + 1, len(list_with_numbers)):
            if list_with_numbers[i] * list_with_numbers[k] == result:
                counter += 1
    if counter == 0:
        print('НЕТ')
    else:
        print('ДА')


quantity_numbers = int(input())

product_of_numbers(quantity_numbers)