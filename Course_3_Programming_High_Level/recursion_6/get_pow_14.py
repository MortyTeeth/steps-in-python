def get_pow(value, degree):
    if degree == 0:
        return 1
    else:
        return value * get_pow(value, degree - 1)
