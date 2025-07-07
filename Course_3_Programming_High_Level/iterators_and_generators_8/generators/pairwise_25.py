def pairwise(iterable):
    try:
        iterator = (i for i in iterable)
        counter = 0

        for i in iterator:
            try:
                if counter == 0:
                    vr = next(iterator)
                    yield (i, vr)
                    counter += 1
                else:
                    yield (vr, i)
                    vr = i
            except:
                pass
        yield (i, None)
    except:
        pass
