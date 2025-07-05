import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            v = func(*args, **kwargs)
            difference = end - start
            new_string = v[:start] + len(v[start:end]) * char + v[end:]
            return new_string

        return wrapper

    return decorator
