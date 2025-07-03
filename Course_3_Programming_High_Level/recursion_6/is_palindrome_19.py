def is_palindrome(string):
    if string == '':
        return True
    elif string[0] != string[-1]:
        return False
    elif string[0] == string[-1] and len(string) > 1:
        return is_palindrome(string[1:-1])
    elif len(string) == 1 or len(string) == 2:
        return True
    else:
        return False
