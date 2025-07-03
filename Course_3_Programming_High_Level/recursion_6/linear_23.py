def linear(nested_lists):
    new_list = []
    for i in nested_lists:
        if isinstance(i, int):
            new_list.append(i)
        elif isinstance(i, list):
            new_list.extend(linear(i))
    return new_list
