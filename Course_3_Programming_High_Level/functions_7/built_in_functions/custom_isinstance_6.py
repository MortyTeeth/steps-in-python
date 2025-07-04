def custom_isinstance(objects, typeinfo):
    counter = 0
    for i in objects:
        if isinstance(i, typeinfo):
            counter += 1
    return counter
