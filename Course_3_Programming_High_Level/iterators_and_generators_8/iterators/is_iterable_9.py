def is_iterable(obj):
    try:
        result = iter(obj)
        return True
    except:
        return False
