from itertools import count


def tabulate(func):
    result = count(1)
    for i in result:
        yield func(i)
