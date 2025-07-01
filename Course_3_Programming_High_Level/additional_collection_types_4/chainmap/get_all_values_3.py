from collections import ChainMap


def get_all_values(chainmap, key):
    new_list = []
    for i in chainmap.maps:
        for k, v in i.items():
            if k == key:
                new_list.append(v)
    if new_list == []:
        return set()
    else:
        return set(new_list)
