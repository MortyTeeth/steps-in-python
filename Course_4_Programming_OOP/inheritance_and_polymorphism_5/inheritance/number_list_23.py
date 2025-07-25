from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            if all(isinstance(i, (int, float)) for i in iterable):
                super().__init__(i for i in iterable)
            else:
                raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def append(self, item):
        if isinstance(item, (int, float)):
            self.data.append(item)
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def extend(self, other):
        if isinstance(other, (type(self), list)) and all(isinstance(i, (int, float)) for i in other):
            self.data.extend(other)
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def insert(self, index, item):
        if isinstance(item, (int, float)):
            self.data.insert(index, item)
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __add__(self, other):
        if all(isinstance(i, (int, float)) for i in other):
            # Возвращаем новый объект NumberList с объединенными данными
            return NumberList(self.data + other)
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __iadd__(self, other):
        if all(isinstance(i, (int, float)) for i in other):
            self.data.extend(other)
            return self
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __setitem__(self, key, value):
        if isinstance(value, (int, float)):
            self.data[key] = value
        else:
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
