from string import ascii_uppercase, ascii_lowercase


def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if name[0] in ascii_uppercase and all([i in ascii_lowercase for i in name[1:]]):
        return len(names) + 1
    else:
        raise ValueError('Имя не является корректным')
