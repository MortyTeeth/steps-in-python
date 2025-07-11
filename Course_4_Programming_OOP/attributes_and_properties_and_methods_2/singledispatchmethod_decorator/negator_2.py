from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register
    def _(self: bool):
        if self % 2 == 0:
            return True
        else:
            return False

    @neg.register
    def _(self: int):
        return -self

    @neg.register
    def _(self: float):
        return -self
