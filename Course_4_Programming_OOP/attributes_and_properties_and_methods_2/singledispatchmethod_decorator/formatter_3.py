from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(self):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    def _(self: int):
        print(f'Целое число: {self}')

    @format.register
    def _(self: float):
        print(f'Вещественное число: {self}')

    @format.register
    def _(self: list):
        print(f'Элементы списка: {", ".join([str(i) for i in self])}')

    @format.register
    def _(self: tuple):
        print(f'Элементы кортежа: {", ".join([str(i) for i in self])}')

    @format.register
    def _(self: dict):
        print(f'Пары словаря: {", ".join([str((k, v)) for k, v in self.items()])}')
