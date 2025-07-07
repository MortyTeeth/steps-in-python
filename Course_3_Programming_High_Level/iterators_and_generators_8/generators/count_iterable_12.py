from collections import Counter


def count_iterable(iterable):
    s = (1 for i in iterable)
    d = Counter(s)[1]
    return d
