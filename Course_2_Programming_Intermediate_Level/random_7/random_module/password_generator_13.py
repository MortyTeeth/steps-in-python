from random import *
from string import *

letter = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))

dig_symbols = set(digits) - set('lI1oO0')
dig_symbols_list = list(dig_symbols)
dig_symbol = sample(dig_symbols_list, 1)
real_dig_symbol = dig_symbol[0]

up_symbols = set(ascii_uppercase) - set('lI1oO0')
up_symbols_list = list(up_symbols)
up_symbol = sample(up_symbols_list, 1)
real_up_symbol = up_symbol[0]

low_symbols = set(ascii_lowercase) - set('lI1oO0')
low_symbols_list = list(low_symbols)
low_symbol = sample(low_symbols_list, 1)
real_low_symbol = low_symbol[0]

min_str = str(real_dig_symbol) + str(real_up_symbol) + str(real_low_symbol)


def generate_password(length):
    return ''.join(sample(letter, length - 3))


def generate_passwords(count, length):
    return [generate_password(length) + min_str for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
