from itertools import pairwise


def max_pair(iterable):
    list_with_pairs = [sum(i) for i in pairwise(iterable)]
    return max(list_with_pairs)
