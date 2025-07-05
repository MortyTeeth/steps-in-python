import functools


def takes(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            typs = list(types)
            arg = [type(i) for i in args]
            kwarg = list({type(kwarg_key) for kwarg, kwarg_key in kwargs.items()})
            arg = arg + kwarg

            for ar in arg:
                if ar not in typs:
                    raise TypeError
                else:
                    pass
            return func(*args, **kwargs)

        return wrapper

    return decorator
