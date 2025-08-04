class MaxCallsException(Exception):
    pass


import functools


class limited_calls:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                if self.start < self.n:
                    self.start += 1
                    value = func(*args, **kwargs)
                    return value
                else:
                    raise MaxCallsException("Превышено допустимое количество вызовов")

        return wrapper
