from math import *

names_func = {'квадрат', 'куб', 'корень', 'модуль', 'синус'}

natural_num, func = int(input()), input()


def math_func(natural_num, func):
    def search_func(func):
        if func == 'квадрат':
            return natural_num ** 2
        elif func == 'куб':
            return natural_num ** 3
        elif func == 'корень':
            return sqrt(natural_num)
        elif func == 'модуль':
            return abs(natural_num)
        elif func == 'синус':
            return sin(natural_num)

    return search_func(func)


print(math_func(natural_num, func))
