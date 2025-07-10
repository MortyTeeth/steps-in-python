from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.area = pi * (self.radius ** 2)
