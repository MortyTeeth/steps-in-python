def interleave(*args):
    spisok = zip(*args)
    return (i for arg in spisok for i in arg)
