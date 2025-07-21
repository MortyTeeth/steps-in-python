import random


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self._attr_name = None
        self._cached_values = {}

    def __set_name__(self, owner, name):
        self._attr_name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        if self.cache:
            if obj not in self._cached_values:
                self._cached_values[obj] = random.randint(self.start, self.end)
            return self._cached_values[obj]
        else:
            return random.randint(self.start, self.end)

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")
