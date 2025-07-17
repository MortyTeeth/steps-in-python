class OrderedSet:
    def __init__(self, iterable=None):
        self._items = list(dict.fromkeys(iterable)) if iterable is not None else []
        self._set = set(self._items)

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def add(self, obj):
        if obj not in self._set:
            self._items.append(obj)
            self._set.add(obj)

    def discard(self, obj):
        if obj in self._set:
            self._items.remove(obj)
            self._set.remove(obj)

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self._items == other._items
        elif isinstance(other, set):
            return set(self._items) == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        return NotImplemented if result is NotImplemented else not result
