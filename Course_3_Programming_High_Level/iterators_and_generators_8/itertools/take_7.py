from itertools import islice


def take(iterable, n):
    result = islice(iterable, n)
    return result
