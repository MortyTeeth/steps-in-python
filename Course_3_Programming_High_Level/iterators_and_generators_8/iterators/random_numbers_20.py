from random import randint


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

        list_with_random = []
        for i in range(self.n):
            list_with_random.append(randint(self.left, self.right))
        obj = iter(list_with_random)

        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)
