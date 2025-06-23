from random import *
import string


def generate_index():
    first_symbol = choice(string.ascii_uppercase)
    second_symbol = choice(string.ascii_uppercase)
    third_symbol = randrange(0, 100)
    forth_symbol = randrange(0, 100)
    fifth_symbol = choice(string.ascii_uppercase)
    sixth_symbol = choice(string.ascii_uppercase)

    index = first_symbol + second_symbol + str(third_symbol) + '_' + str(forth_symbol) + fifth_symbol + sixth_symbol

    return index


generate_index()
