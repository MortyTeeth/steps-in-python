def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        a = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return a

    return wrapper
