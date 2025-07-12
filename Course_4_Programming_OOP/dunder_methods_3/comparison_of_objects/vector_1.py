class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return (self.x, self.y) == other
        elif isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
