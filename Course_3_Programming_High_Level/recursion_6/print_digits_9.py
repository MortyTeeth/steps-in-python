def print_digits(number):
    str_num = str(number)
    if len(str_num) > 0:
        print(str_num[0])
        str_num = str_num[1:]
        print_digits(str_num)
