class Row:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __repr__(self):
        return f'Row({", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items()])})'

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            raise AttributeError('Установка нового атрибута невозможна')

    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self._fields.items()) == tuple(other._fields.items())
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self._fields))

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    @property
    def _fields(self):
        return self.__dict__
