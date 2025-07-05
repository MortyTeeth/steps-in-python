def takes_positive(func):
    def wrapper(*args, **kwargs):
        counter = 0
        args = [i for i in args]
        kwargs = {l: o for l, o in kwargs.items()}
        for k in args:
            if isinstance(k, int):
                if k > 0:
                    counter += 1
                else:
                    return f"<class 'ValueError'>"

            else:
                return f"<class 'TypeError'>"

        for key, value in kwargs.items():
            if isinstance(value, int):
                if value > 0:
                    counter += 1
                else:
                    return f"<class 'ValueError'>"

            else:
                return f"<class 'TypeError'>"

        if counter == len(args) + len(kwargs):
            return func(*args, **kwargs)

    return wrapper
