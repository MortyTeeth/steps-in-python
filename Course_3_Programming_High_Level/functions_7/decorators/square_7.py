import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return val ** 2

    return wrapper
