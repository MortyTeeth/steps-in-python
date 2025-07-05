import functools


def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(func(*args, **kwargs), datatype):
                return func(*args, **kwargs)
            else:
                raise TypeError

        return wrapper

    return decorator
