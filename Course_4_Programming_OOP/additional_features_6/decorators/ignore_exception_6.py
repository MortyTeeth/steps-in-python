import functools


class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as er:
                if type(er) in self.args:
                    print(f"Исключение {er.__class__.__name__} обработано")
                else:
                    raise er

        return wrapper
