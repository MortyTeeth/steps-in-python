class Summator:
    pass

    def total(self, n, m=1):
        return sum(i ** m for i in range(1, n + 1))


class SquareSummator(Summator):
    def total(self, n, m=1):
        return super().total(n, m=2)


class QubeSummator(Summator):
    def total(self, n, m=1):
        return super().total(n, m=3)


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n, m=1):
        return super().total(n, m=self.m)
