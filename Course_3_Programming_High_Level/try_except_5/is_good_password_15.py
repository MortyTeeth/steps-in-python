from string import ascii_uppercase, ascii_lowercase

rus_alph = 'йцукенгшщзхъфывапролджэячсмитьбюё'
big_rus_alph = rus_alph.upper()


def is_good_password(string):
    if len(string) >= 9 and any(i in ascii_uppercase for i in string) and any(
            i in ascii_lowercase for i in string) and any(i.isdigit() for i in string) or len(string) >= 9 and any(
        i in rus_alph for i in string) and any(i in big_rus_alph for i in string) and any(
        i.isdigit() for i in string):
        return True
    else:
        return False
