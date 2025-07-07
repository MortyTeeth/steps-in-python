def around(iterable):
    iterable = list(iterable)
    if not iterable:
        return

    if len(iterable) == 1:
        yield (None, iterable[0], None)
        return

    yield (None, iterable[0], iterable[1])

    for prev, curr, nxt in zip(iterable, iterable[1:], iterable[2:]):
        yield (prev, curr, nxt)

    yield (iterable[-2], iterable[-1], None)
