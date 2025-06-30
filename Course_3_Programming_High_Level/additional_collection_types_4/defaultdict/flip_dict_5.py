from collections import defaultdict


def flip_dict(dict_of_lists):
    result = defaultdict(list)
    for key, value in dict_of_lists.items():
        for val in value:
            result[val].append(key)

    return result
