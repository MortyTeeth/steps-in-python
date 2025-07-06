def filterfalse(predicate, iterable):
    result = list(filter(predicate, iterable))
    new_list = [i for i in iterable if i not in result]
    return new_list
