from string import ascii_lowercase, ascii_uppercase

d = {0: 'в пароле нет ни одной буквы',
     1: 'в пароле нет ни одной заглавной буквы',
     2: 'в пароле нет ни одной строчной буквы',
     3: 'в пароле нет ни одной цифры'}


def verification(login, password, success, failure):
    if not any(c for c in password if c in ascii_uppercase + ascii_lowercase):
        return failure(login, d[0])
    if not any(c in ascii_lowercase for c in password):
        return failure(login, d[2])
    if not any(c in ascii_uppercase for c in password):
        return failure(login, d[1])
    if not any(c in '1234567890' for c in password):
        return failure(login, d[3])
    else:
        return success(login)
