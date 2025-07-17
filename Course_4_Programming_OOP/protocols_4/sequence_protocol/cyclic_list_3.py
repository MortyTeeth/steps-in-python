import itertools


class CyclicList:
    def __init__(self, iterable=None):
        self.iterable = list(iterable) if iterable is not None else []
        self.cycle = itertools.cycle(self.iterable)

    def check_key(self, key):
        if not isinstance(key, int):
            raise TypeError
        if not self.iterable:
            raise IndexError
        return key % len(self.iterable)

    def __getitem__(self, key):
        key = self.check_key(key)
        return self.iterable[key]

    def __setitem__(self, key, value):
        key = self.check_key(key)
        self.iterable[key] = value
        self.cycle = itertools.cycle(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cycle)

    def __len__(self):
        return len(self.iterable)

    def append(self, obj):
        self.iterable.append(obj)
        self.cycle = itertools.cycle(self.iterable)

    def pop(self, index=None):
        if index is None:
            index = -1
        elem = self.iterable.pop(index)
        self.cycle = itertools.cycle(self.iterable)
        return elem
