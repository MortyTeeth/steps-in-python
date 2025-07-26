from collections.abc import Iterable, Iterator


def is_iterable(value):
    return True if isinstance(value, Iterable) else False


def is_iterator(value):
    return True if isinstance(value, Iterator) else False
