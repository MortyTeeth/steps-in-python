class AttrsIterator:
    def __init__(self, obj):
        self._attributes = list(obj.__dict__.items())
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._attributes):
            raise StopIteration
        value = self._attributes[self._index]
        self._index += 1
        return value
