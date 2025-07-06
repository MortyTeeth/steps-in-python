class Square:
    def __init__(self, n, iteration=1):
        self.n = n
        self.iteration = iteration

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration - self.n == 1:
            raise StopIteration
        else:
            value = self.iteration ** 2
            self.iteration += 1
        return value
