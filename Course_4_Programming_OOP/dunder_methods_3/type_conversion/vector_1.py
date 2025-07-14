class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __int__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __float__(self):
        return float((self.x ** 2 + self.y ** 2) ** 0.5)

    def __complex__(self):
        if self.y < 0:
            return complex(f"({self.x}{self.y}j)")
        return complex(f"({self.x}+{self.y}j)")

    def __bool__(self):
        return True if any([bool(self.x), bool(self.y)]) else False
