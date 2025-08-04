import functools


class exception_decorator:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return (value, None)
        except Exception as er:
            return (None, type(er))
