def first_true(iterable, predicate):
    result = list(filter(predicate, iterable))
    for i in result:
        if i != False:
            return i
        else:
            return None
