from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    @staticmethod
    def process(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register
    def _(self: int):
        return self * 2

    @process.register
    def _(self: float):
        return self * 2

    @process.register
    def _(self: str):
        return self.upper()

    @process.register
    def sorted_tuple(self: tuple):
        return tuple(sorted(list(self)))

    @process.register
    def sorted_list(self: list):
        return sorted(self)
