class SuperInt(int):
    def __new__(cls, value):
        return super().__new__(cls, int(value))

    def __init__(self, value):
        pass

    def repeat(self, n=2):
        abs_part = str(abs(self)) * n
        if self < 0:
            return SuperInt('-' + abs_part)
        return SuperInt(abs_part)

    def to_bin(self):
        binary = bin(abs(self))[2:]
        if self < 0:
            return '-' + binary
        return binary

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        for digit in str(abs(self)):
            yield SuperInt(digit)
