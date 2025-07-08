def take_nth(iterable, n):
    try:
        result = list(iterable)
        return result[n - 1]
    except:
        return None
