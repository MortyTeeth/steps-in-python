def mean(*args):
    s = sum([i for i in args if isinstance(i, (int, float)) and type(i) != bool])
    l = len([i for i in args if isinstance(i, (int, float)) and type(i) != bool])
    if l == 0:
        return 0.0
    else:
        return float(s / l)
