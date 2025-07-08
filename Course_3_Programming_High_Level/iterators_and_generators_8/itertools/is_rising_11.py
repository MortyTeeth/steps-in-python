from itertools import pairwise


def is_rising(iterable):
    true_and_false_list = []
    pairwise_list = list(pairwise(iterable))
    for i in pairwise_list:
        if i[0] < i[1]:
            true_and_false_list.append(True)
        else:
            true_and_false_list.append(False)
    if all(true_and_false_list):
        return True
    else:
        return False
