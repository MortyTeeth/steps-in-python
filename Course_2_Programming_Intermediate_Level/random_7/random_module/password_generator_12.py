import string
from random import *


def generate_password(num, length):
    escape_symbols = 'lI1oO0'
    symbols = string.ascii_letters + string.digits
    real_length = length
    for i in range(num):
        length = real_length
        enemy_str = ''
        while length > 0:
            a = sample(symbols, 1)
            p = a[0]
            if p not in escape_symbols:
                enemy_str += str(p)
                length -= 1
        print(enemy_str)


num_pass = int(input())
length_pass = int(input())

generate_password(num_pass, length_pass)
