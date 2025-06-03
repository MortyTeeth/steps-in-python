number = int(input())

if 0 <= number <= 36:
    if number == 0:
        print('зеленый')
    elif (0 < number <= 10) and (number % 2 == 0):
        print('черный')
    elif (0 < number <= 10) and (number % 2 == 1):
        print('красный')
    elif (10 < number <= 18) and (number % 2 == 0):
        print('красный')
    elif (10 < number <= 18) and (number % 2 == 1):
        print('черный')
    elif (18 < number <= 28) and (number % 2 == 0):
        print('черный')
    elif (18 < number <= 28) and (number % 2 == 1):
        print('красный')
    elif (28 < number <= 36) and (number % 2 == 0):
        print('красный')
    elif (28 < number <= 36) and (number % 2 == 1):
        print('черный')
else:
    print('ошибка ввода')