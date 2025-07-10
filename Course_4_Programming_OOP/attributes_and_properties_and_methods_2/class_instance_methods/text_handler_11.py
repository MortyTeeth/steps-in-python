class TextHandler:
    def __init__(self):
        self.iterable = []
        pass

    def add_words(self, text):
        split_text = text.split()
        for word in split_text:
            self.iterable.append(word)

    def get_shortest_words(self):
        if len(self.iterable) < 1:
            return []
        else:
            min_len = min([len(i) for i in self.iterable])
            return [i for i in self.iterable if len(i) == min_len]

    def get_longest_words(self):
        if len(self.iterable) < 1:
            return []
        else:
            max_len = max([len(i) for i in self.iterable])
            return [i for i in self.iterable if len(i) == max_len]
