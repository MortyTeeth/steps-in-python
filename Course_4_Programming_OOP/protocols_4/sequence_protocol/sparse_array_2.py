for_check = []


class SparseArray:
    def __init__(self, default):
        self.default = default
        self.list = list(range(0, 100000))

    def check_key(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key < 0:
            raise IndexError
        return key

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key < 0 or key >= len(self.list):
            raise IndexError('Неверный индекс')
        if key not in for_check:
            return self.default
        return self.list[key]

    def __setitem__(self, key, value):
        key = self.check_key(key)
        self.list[key] = value
        for_check.append(key)
