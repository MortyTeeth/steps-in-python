from string import ascii_lowercase, ascii_uppercase

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


class StrExtension:
    def __init__(self):
        pass

    @staticmethod
    def remove_vowels(string):
        return ''.join([i for i in string if i not in vowels])

    @staticmethod
    def leave_alpha(string):
        return ''.join([i for i in string if i in ascii_uppercase + ascii_lowercase])

    @staticmethod
    def replace_all(string, chars, char):
        for i in chars:
            string = string.replace(i, char)
        return string
