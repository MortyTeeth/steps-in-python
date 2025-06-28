import time


def calculate_it(func, *args):
    start = time.time()
    return (func(*args), time.time() - start)
