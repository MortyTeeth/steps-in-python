class TypeChecked:
    def __init__(self, *args):
        self._types = args

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        elif self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if isinstance(value, self._types):
            obj.__dict__[self.name] = value
        else:
            raise TypeError("Некорректное значение")

    def __delete__(self, obj):
        del obj.__dict__[self.name]
