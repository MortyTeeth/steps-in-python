class RandomLooper:
    def __init__(self, *args):
        self.args = [item for sublist in args for item in sublist]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.args):
            raise StopIteration
        value = self.args[self.index]
        self.index += 1
        return value
