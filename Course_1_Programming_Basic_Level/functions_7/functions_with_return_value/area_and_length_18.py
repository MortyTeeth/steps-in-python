from math import pi


def get_circle(radius):
    C = 2 * pi * radius
    S = pi * radius ** 2
    return C, S


r = float(input())

length, square = get_circle(r)
print(length, square)
