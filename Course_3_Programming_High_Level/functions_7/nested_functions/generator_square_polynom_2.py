def generator_square_polynom(a, b, c):
    def x(x):
        return a * (x ** 2) + b * x + c

    return x
