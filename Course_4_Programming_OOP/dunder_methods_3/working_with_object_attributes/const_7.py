class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            self.__dict__[key] = value
