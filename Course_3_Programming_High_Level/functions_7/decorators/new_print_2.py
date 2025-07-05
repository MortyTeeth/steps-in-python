def new_print(func):
    def wrapper(*args, **kwargs):
        args = [str(arg).upper() for arg in args]
        kwargs = {kwarg: kwarg_key.upper() for kwarg, kwarg_key in kwargs.items()}
        func(*args, **kwargs)

    return wrapper


print = new_print(print)
