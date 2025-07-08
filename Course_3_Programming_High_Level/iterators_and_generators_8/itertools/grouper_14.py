from itertools import zip_longest


def grouper(iterable, n):
    iterator = iter(iterable)
    l = [iter(iterator) for i in range(n)]
    return zip_longest(*l)
