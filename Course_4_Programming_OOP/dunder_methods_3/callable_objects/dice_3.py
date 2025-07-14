from random import randint


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self, *args, **kwargs):
        self.random_int = randint(1, self.sides)
        return self.random_int
