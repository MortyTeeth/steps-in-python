import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        if type(func(*args, **kwargs)) == int or type(func(*args, **kwargs)) == list:
            print(f"TRACE: возвращаемое значение {func.__name__}(): {func(*args, **kwargs)}")
        else:
            print(f"TRACE: возвращаемое значение {func.__name__}(): '{func(*args, **kwargs)}'")
        return func(*args, **kwargs)

    return wrapper
