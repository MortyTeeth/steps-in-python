import functools


def ignore_exception(*types_of_exceptions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            exceptions = list(types_of_exceptions)
            if len(types_of_exceptions) != 0:
                try:
                    value = func(*args, **kwargs)
                    return value
                except Exception as err:
                    if type(err) in exceptions:
                        print(f'Исключение {str(err.__class__)[8:-2]} обработано')
                    elif type(err) not in exceptions:
                        func(*args, **kwargs)
                    else:
                        return type(err)

            else:
                func(*args, **kwargs)

        return wrapper

    return decorator
