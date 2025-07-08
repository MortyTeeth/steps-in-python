def first_largest(iterable, number):
    obj = list(iterable)
    for i in range(len(obj)):
        if obj[i] > number:
            return i

    return -1
