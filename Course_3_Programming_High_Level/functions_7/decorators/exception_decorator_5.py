def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, int):
                return f"({result}, 'Функция выполнилась без ошибок')"
            else:
                return f"('{result}', 'Функция выполнилась без ошибок')"
        except:
            return f"(None, 'При вызове функции произошла ошибка')"

    return wrapper
