class Shape:
    __slots__ = ("name", "color", "area")

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f"{self.color} {self.name} ({self.area})"

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area == other.area

    def __gt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area > other.area

    def __ge__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        else:
            return self.area >= other.area
