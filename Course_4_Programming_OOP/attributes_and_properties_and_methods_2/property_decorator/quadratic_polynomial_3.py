class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        x1 = (-self.b - ((self.b ** 2) - (4 * self.a * self.c)) ** 0.5) / (2 * self.a)
        if isinstance(x1, int) or isinstance(x1, float):
            return x1
        else:
            return None

    @property
    def x2(self):
        x2 = (-self.b + ((self.b ** 2) - (4 * self.a * self.c)) ** 0.5) / (2 * self.a)
        if isinstance(x2, int) or isinstance(x2, float):
            return x2
        else:
            return None

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, value):
        self.a = value[0]
        self.b = value[1]
        self.c = value[2]
