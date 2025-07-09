def is_decimal(string):
    try:
        number = float(string)
        return True
    except:
        return False
