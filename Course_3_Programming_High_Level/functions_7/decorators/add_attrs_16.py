import functools


def add_attrs(**strings):
    def decorator(func):
        for k, v in strings.items():
            func.__dict__[k] = v

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator
