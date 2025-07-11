class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, value):
        return cls(value[0], value[1], value[2])

    @classmethod
    def from_str(cls, str):
        value = [float(i) for i in str.split()]
        return cls(value[0], value[1], value[2])
