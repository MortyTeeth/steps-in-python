from string import ascii_lowercase


class Alphabet:
    def __init__(self, language):
        self.language = language
        self.iteration = 0

        if self.language == 'ru':
            self.alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        elif self.language == 'en':
            self.alphabet = ascii_lowercase

        self.iterator = iter(self.alphabet)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            letter = next(self.iterator)
            self.iteration += 1
            return letter
        except:
            self.iterator = iter(self.alphabet)
            self.iteration = 0
            return next(self.iterator)
