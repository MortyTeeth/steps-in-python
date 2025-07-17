class Grouper:
    def __init__(self, iterable, key):
        self._key = key
        self._iterable = dict()
        for i in iterable:
            if self._key(i) not in self._iterable:
                self._iterable.update({self._key(i): [i]})
            else:
                self._iterable[self._key(i)].append(i)

    def __len__(self):
        return len(self._iterable)

    def __iter__(self):
        return iter(self._iterable.items())

    def add(self, i):
        if self._key(i) not in self._iterable:
            self._iterable.update({self._key(i): [i]})
        else:
            self._iterable[self._key(i)].append(i)

    def group_for(self, obj):
        hz = self._key(obj)
        return hz

    def __getitem__(self, key):
        return self._iterable[key]

    def __contains__(self, item):
        return item in self._iterable
