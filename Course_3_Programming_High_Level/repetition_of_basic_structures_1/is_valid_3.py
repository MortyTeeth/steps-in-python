def is_valid(string):
    if 4 <= len(string) <= 6 and ' ' not in string and string != '' and string.isdigit():
        return True
    else:
        return False
