class Wordplay:
    def __init__(self, words=None):
        self.words = list(words) if words else []

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        allowed_set = set(args)
        return [word for word in self.words if set(word).issubset(allowed_set)]

    def avoid(self, *args):
        forbidden_set = set(args)
        return [word for word in self.words if set(word).isdisjoint(forbidden_set)]


words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
