from string import ascii_uppercase, ascii_lowercase, digits

rus_alph = 'йцукенгшщзхъфывапролджэячсмитьбюё'
big_rus_alph = rus_alph.upper()


class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    has_upper = any(i in ascii_uppercase for i in string) or any(i in big_rus_alph for i in string)
    has_lower = any(i in ascii_lowercase for i in string) or any(i in rus_alph for i in string)

    if not (has_upper and has_lower):
        raise LetterError
    if not any(i.isdigit() for i in string):
        raise DigitError
    return True
