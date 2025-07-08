from string import ascii_uppercase
from itertools import cycle


def alnum_sequence():
    result = (i for i in zip(cycle(range(1, 27)), cycle(ascii_uppercase)))
    for i in result:
        yield from i
