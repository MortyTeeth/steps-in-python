import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        if isinstance(val, str):
            return val
        else:
            raise TypeError

    return wrapper
