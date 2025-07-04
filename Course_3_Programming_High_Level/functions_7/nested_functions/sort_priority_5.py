def sort_priority(values, group):
    non = set(group) - set(values)
    new_group = set(group) - non
    values[:] = sorted(list(new_group)) + sorted(list(set(values) - new_group))
    return values
