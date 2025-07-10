class Numbers:
    def __init__(self):
        self.iterable = []
        pass

    def add_number(self, int_num):
        self.iterable.append(int_num)

    def get_even(self):
        return [i for i in self.iterable if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.iterable if i % 2 == 1]
