from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return f"{self.word.title()}"

    def __repr__(self):
        return f"Word('{self.word}')"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
