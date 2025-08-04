import functools


class takes_numbers:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        if all(isinstance(i, (int, float)) for i in args) and all(isinstance(v, (int, float)) for v in kwargs.values()):
            return self.func(*args, **kwargs)
        else:
            raise TypeError("Аргументы должны принадлежать типам int или float")
