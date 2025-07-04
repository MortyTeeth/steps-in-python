def zip_longest(*args, fill=None):
    max_len_in_args = len(max(args, key=lambda x: len(x)))
    for arg in args:
        if len(arg) == max_len_in_args:
            pass
        else:
            while len(arg) != max_len_in_args:
                arg.append(fill)
    list_with_zip = list(zip(*args))

    return list_with_zip
