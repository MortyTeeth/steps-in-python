from random import *


def generate_ip():
    first_num = randrange(0, 256)
    second_num = randrange(0, 256)
    third_num = randrange(0, 256)
    fourth_num = randrange(0, 256)

    ip = str(first_num) + '.' + str(second_num) + '.' + str(third_num) + '.' + str(fourth_num)

    return ip


generate_ip()
