import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times - 1):
                func(*args, **kwargs)
            value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator
