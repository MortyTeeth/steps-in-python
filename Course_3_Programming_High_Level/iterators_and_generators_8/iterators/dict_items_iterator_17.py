class DictItemsIterator:
    def __init__(self, data):
        self.data = iter(data.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)
