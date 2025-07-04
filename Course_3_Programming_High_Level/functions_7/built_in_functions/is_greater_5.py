def is_greater(lists, number):
    if any([True for i in lists if sum(i) > number]):
        return True
    else:
        return False
