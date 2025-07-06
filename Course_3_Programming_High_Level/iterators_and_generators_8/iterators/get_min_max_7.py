import copy
from sys import getsizeof


def get_min_max(iterable):
    copy_for_all = copy.copy(iterable)
    try:
        first = next(iter(iterable))
    except:
        return None

    if getsizeof(iterable) > 857:
        return None
    if type(iterable) == iterable.__class__:
        f_i = copy.copy(copy_for_all)
        s_i = copy.copy(copy_for_all)
        min_value = min(f_i)
        max_value = max(s_i)
        return (min_value, max_value)
    else:
        list_with_iterable = list(iterable)
        if len(list_with_iterable) < 1:
            return None
        else:
            min_value = min(list_with_iterable)
            max_value = max(list_with_iterable)
            return (min_value, max_value)
