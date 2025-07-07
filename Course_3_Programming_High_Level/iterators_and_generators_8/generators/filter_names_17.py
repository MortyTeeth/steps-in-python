def filter_names(names, ignore_char, max_names):
    filter_with_ignore_char = (i for i in names if i[0] != ignore_char and i[0].lower() != ignore_char)
    filter_with_ignore_digits = list((i for i in filter_with_ignore_char if not any(symbol.isdigit() for symbol in i)))

    if len(filter_with_ignore_digits) < max_names:
        yield from filter_with_ignore_digits
    else:
        for k in range(max_names):
            yield filter_with_ignore_digits[k]
