from itertools import chain


def sum_of_digits(iterable):
    list_iterable = [str(i) for i in iterable]
    chain_list = [int(i) for i in chain.from_iterable(list_iterable)]
    return sum(chain_list)
