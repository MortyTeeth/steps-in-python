class ModularTuple(tuple):
    def __new__(cls, iterable=[], size=100):
        instance = super().__new__(cls, [i % size for i in iterable])
        instance.size = size
        return instance

    def __init__(self, iterable=[], size=100):
        pass
