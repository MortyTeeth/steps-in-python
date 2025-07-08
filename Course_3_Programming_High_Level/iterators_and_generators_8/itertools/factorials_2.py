from itertools import accumulate


def factorials(n):
    result = list(accumulate(list(range(1, n + 1)), lambda x, y: x * y))
    yield from result
