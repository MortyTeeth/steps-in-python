from itertools import tee, chain


def ncycles(iterable, times):
    list_with_iterators = [i for i in tee(iterable, times)]
    return chain.from_iterable(list_with_iterators)
