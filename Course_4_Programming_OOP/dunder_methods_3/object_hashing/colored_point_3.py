class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def __repr__(self):
        return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    @property
    def _fields(self):
        return self._x, self._y, self._color

    def get_color(self):
        return self._color

    def set_color(self, color):
        raise AttributeError

    color = property(get_color, set_color)

    def get_x(self):
        return self._x

    def set_x(self, x):
        raise AttributeError

    x = property(get_x, set_x)

    def get_y(self):
        return self._y

    def set_y(self, y):
        raise AttributeError

    y = property(get_y, set_y)
