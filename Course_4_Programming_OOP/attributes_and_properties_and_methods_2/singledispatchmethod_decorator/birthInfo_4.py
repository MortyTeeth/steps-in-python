from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def _(self, birth_date: str):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def _(self, birth_date: date):
        self.birth_date = birth_date

    @__init__.register
    def _(self, birth_date: list):
        try:
            self.birth_date = date(*birth_date)
        except (TypeError, ValueError):
            raise TypeError('Аргумент переданного типа не поддерживается') from None

    @__init__.register
    def _(self, birth_date: tuple):
        try:
            self.birth_date = date(*birth_date)
        except (TypeError, ValueError):
            raise TypeError('Аргумент переданного типа не поддерживается') from None

    @property
    def age(self):
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years
