class AttrsNumberObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value
        self.__dict__.update({'attrs_num': 'attrs_num'})

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    @property
    def attrs_num(self):
        return len(self.__dict__)
