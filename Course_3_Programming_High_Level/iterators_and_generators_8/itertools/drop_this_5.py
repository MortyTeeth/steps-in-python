from itertools import dropwhile


def drop_this(iterable, obj):
    result = dropwhile(lambda x: x == obj, iterable)
    yield from result
