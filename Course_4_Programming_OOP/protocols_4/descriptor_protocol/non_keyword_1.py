from keyword import kwlist


class NonKeyword:
    def __init__(self, name):
        self._name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError("Некорректное значение")
        elif len(str(value)) > 0:
            obj.__dict__[self._name] = value
        else:
            raise ValueError("Некорректное значение")

    def __delete__(self, instance):
        del object.__dict__[self._name]
