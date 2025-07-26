from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = list(iterable)

    def __getitem__(self, item):
        return self.iterable[item]

    def __len__(self):
        return len(self.iterable)

    def __str__(self):
        return f"{self.iterable}"

    def __invert__(self):
        return BitArray([0 if i == 1 else 1 for i in self.iterable])

    def __or__(self, other):
        if not isinstance(other, (BitArray, list)):
            return NotImplemented
        if len(self.iterable) != len(other.iterable):
            raise TypeError
        return BitArray(x | y for x, y in zip(self.iterable, other.iterable))

    def __and__(self, other):
        if not isinstance(other, (BitArray, list)):
            return NotImplemented
        if len(self.iterable) != len(other.iterable):
            raise TypeError
        return BitArray(x & y for x, y in zip(self.iterable, other.iterable))
