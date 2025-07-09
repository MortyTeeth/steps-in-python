def quantify(iterable, predicate):
    result = list((i for i in iterable))
    count = 0
    if predicate != None:
        for i in result:
            if predicate(i) == True:
                count += 1
        return count
    else:
        predicate = bool
        for i in result:
            if predicate(i) == True:
                count += 1
        return count
