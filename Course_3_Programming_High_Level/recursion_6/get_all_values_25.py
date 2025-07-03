def get_all_values(nested_dicts, key):
    result = set()
    for value in nested_dicts.values():
        if type(value) == dict:
            value = get_all_values(value, key)
            result.update(value)
        else:
            if key in nested_dicts:
                result.add(nested_dicts[key])

    return result
