months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
               9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def months(number):
    try:
        int_number = int(number)
        if 1 <= int_number <= 12:
            print(months_dict[int_number])
        else:
            print('Введено число из недопустимого диапазона')
    except:
        print('Введено некорректное значение')


month_number = input()
months(month_number)
