def with_previous(iterable):
    iterator = (i for i in iterable)
    counter = 0
    for i in iterator:
        if counter == 0:
            yield (i, None)
            counter += 1
            vr = i
        else:
            yield (i, vr)
            vr = i
