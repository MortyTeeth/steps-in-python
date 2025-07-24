class AdvancedTuple(tuple):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        pass

    def __add__(self, other):
        try:
            return AdvancedTuple(tuple(self) + tuple(other))
        except:
            return NotImplemented

    def __radd__(self, other):
        try:
            return tuple(other).__add__(tuple(self))
        except:
            return NotImplemented
