def is_iterator(obj):
    return True if '__next__' in dir(obj) else False
