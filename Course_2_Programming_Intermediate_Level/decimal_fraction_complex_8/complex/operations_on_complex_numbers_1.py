from cmath import *


def operations_on_complex_numbers(f_c_n, s_c_n):
    first_complex_num = complex(f_c_n)
    second_complex_num = complex(s_c_n)

    print(
        str(first_complex_num) + ' + ' + str(second_complex_num) + ' = ' + str(first_complex_num + second_complex_num))
    print(
        str(first_complex_num) + ' - ' + str(second_complex_num) + ' = ' + str(first_complex_num - second_complex_num))
    print(
        str(first_complex_num) + ' * ' + str(second_complex_num) + ' = ' + str(first_complex_num * second_complex_num))


first_complex_num, second_complex_num = input(), input()

operations_on_complex_numbers(first_complex_num, second_complex_num)
