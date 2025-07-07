def flatten(nested_list):
    for nest in nested_list:
        if type(nest) == int:
            yield nest
        else:
            yield from flatten(nest)
