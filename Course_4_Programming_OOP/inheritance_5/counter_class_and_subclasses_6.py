class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, num=None):
        if num is None:
            self.value += 1
        else:
            self.value += num

    def dec(self, num=None):
        if num is None:
            self.value -= 1
        else:
            self.value -= num

        if self.value <= 0:
            self.value = 0


class NonDecCounter(Counter):
    def __init__(self, start=0):
        Counter.__init__(self, start=0)
        self.value = start

    def dec(self, num=None):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start=0)
        self.value = start
        self.limit = limit

    def inc(self, num=None):
        if num is None:
            self.value += 1
        else:
            self.value += num

        if self.value >= self.limit:
            self.value = self.limit
