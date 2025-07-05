import functools


def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end == False:
                return string + func(*args, **kwargs)
            else:
                return func(*args, **kwargs) + string

        return wrapper

    return decorator
