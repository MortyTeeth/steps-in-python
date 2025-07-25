class AdvancedList(list):
    def __init__(self, iterable):
        super().__init__(i for i in iterable)
        self.iterable = iterable

    def join(self, str_arg=' '):
        return str_arg.join(str(i) for i in self.iterable)

    def map(self, func):
        self[:] = [func(i) for i in self.iterable]
        return self

    def filter(self, func):
        self[:] = [i for i in self.iterable if func(i) != False]
