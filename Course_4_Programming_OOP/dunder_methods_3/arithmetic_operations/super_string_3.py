class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, SuperString):
            return self.__add__(other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.__mul__(other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            part = len(self.string) // other
            return SuperString(self.string[:part])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other == 0:
                return SuperString(self.string)
            elif other >= len(self.string):
                return SuperString('')
            else:
                return SuperString(self.string[:-other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return SuperString('' if other >= len(self.string) else self.string[other:])
        return NotImplemented
