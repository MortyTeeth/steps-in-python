def unique(iterable):
    new_list = []
    for i in iterable:
        if i not in new_list:
            new_list.append(i)
    yield from new_list
