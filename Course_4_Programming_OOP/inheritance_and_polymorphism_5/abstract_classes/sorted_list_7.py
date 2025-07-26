from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = sorted(iterable)

    def add(self, obj):
        self.iterable.append(obj)
        self.iterable.sort()

    def discard(self, obj):
        self.iterable = [i for i in self.iterable if i != obj]

    def update(self, value):
        self.iterable.extend(value)
        self.iterable.sort()

    def __repr__(self):
        return f"SortedList({self.iterable})"

    def append(self, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def extend(self, value):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        return iter(self.iterable)

    def __contains__(self, item):
        return item in self.iterable

    def __getitem__(self, item):
        return self.iterable[item]

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self.iterable + other.iterable)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self.iterable += other.iterable
            self.iterable.sort()
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SortedList(self.iterable * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.iterable *= other
            self.iterable.sort()
            return self
        return NotImplemented

    def __delitem__(self, key):
        del self.iterable[key]

    def __eq__(self, other):
        if isinstance(other, SortedList):
            return self.iterable == other.iterable
        return NotImplemented
