def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]

    for value in nested_dicts.values():
        if isinstance(value, dict):
            value = get_value(value, key)
            if value is not None:
                return value
