class HistoryDict:
    def __init__(self, data=None):
        self._data = {}
        if data is not None:
            for key, value in data.items():
                self._data[key] = [value]

    def keys(self):
        return self._data.keys()

    def values(self):
        return [v[-1] for v in self._data.values()]

    def items(self):
        return [(k, v[-1]) for k, v in self._data.items()]

    def history(self, key):
        return self._data.get(key, [])

    def all_history(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key][-1]

    def __setitem__(self, key, value):
        if key not in self._data:
            self._data[key] = []
        self._data[key].append(value)

    def __delitem__(self, key):
        del self._data[key]
