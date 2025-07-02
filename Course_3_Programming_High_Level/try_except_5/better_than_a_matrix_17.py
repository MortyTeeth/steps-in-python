from string import ascii_uppercase, ascii_lowercase, digits
import sys

rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus_upper = rus_lower.upper()


class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError

    has_upper = any(i in ascii_uppercase or i in rus_upper for i in string)
    has_lower = any(i in ascii_lowercase or i in rus_lower for i in string)
    has_digit = any(i in digits for i in string)

    if not (has_upper and has_lower):
        raise LetterError
    if not has_digit:
        raise DigitError

    return True


for line in sys.stdin:
    password = line.strip()
    if not password:
        continue
    try:
        if is_good_password(password):
            print("Success!")
            break
    except Exception as err:
        print(type(err).__name__)
