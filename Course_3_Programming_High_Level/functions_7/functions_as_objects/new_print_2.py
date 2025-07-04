old_print = print


def new_print(*args, sep=None, end=None):
    list_with_args = []
    for arg in args:
        if isinstance(arg, str):
            list_with_args.append(arg.upper())
        else:
            list_with_args.append(arg)
    if sep == None and end == None:
        old_print(*list_with_args)
    else:
        old_print(*list_with_args, sep=sep.upper(), end=end.upper())


print = new_print
