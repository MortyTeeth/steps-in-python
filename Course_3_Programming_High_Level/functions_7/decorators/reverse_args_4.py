def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = reversed(args)
        return func(*args, **kwargs)

    return wrapper
