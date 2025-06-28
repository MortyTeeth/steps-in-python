import time


def get_the_fastest_func(funcs, arg):
    dict_with_name_func_and_delta = {}
    for func in funcs:
        start = time.time()
        func(arg)
        end = time.time()
        delta = end - start
        dict_with_name_func_and_delta[delta] = func

    # Найти минимальное время выполнения
    min_time = min(dict_with_name_func_and_delta)
    # Вернуть соответствующую функцию
    return dict_with_name_func_and_delta[min_time]
