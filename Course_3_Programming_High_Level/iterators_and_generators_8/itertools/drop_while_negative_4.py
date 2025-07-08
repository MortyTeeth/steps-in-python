from itertools import filterfalse, takewhile, dropwhile


def drop_while_negative(iterable):
    yield from dropwhile(lambda x: x < 0, iterable)
