from collections import ChainMap


def deep_update(chainmap, key, value):
    found = False

    for dictionary in chainmap.maps:
        if key in dictionary:
            dictionary[key] = value
            found = True

    if not found:
        chainmap.maps[0][key] = value
