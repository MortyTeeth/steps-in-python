from abc import abstractmethod


class Stat:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = list(iterable)

    def add(self, num):
        self.iterable.append(num)

    @abstractmethod
    def result(self):
        pass

    def clear(self):
        self.iterable.clear()


class MinStat(Stat):
    def result(self):
        return min(self.iterable, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self.iterable, default=None)


class AverageStat(Stat):
    def result(self):
        if len(self.iterable) < 1:
            return None
        else:
            return sum(self.iterable) / len(self.iterable)
