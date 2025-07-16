class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self.real_step = self.n + 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        value = self.iterable[self.index]
        self.index += self.real_step
        return value
