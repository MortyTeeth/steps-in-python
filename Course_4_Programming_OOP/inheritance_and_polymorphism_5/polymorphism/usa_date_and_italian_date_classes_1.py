from datetime import date
from abc import abstractmethod


class Date:
    def __init__(self, year, month, day):
        self._date = date(year=year, month=month, day=day)

    def iso_format(self):
        return self._date

    @abstractmethod
    def format(self):
        pass


class USADate(Date):
    def format(self):
        return self._date.strftime("%m-%d-%Y")


class ItalianDate(Date):
    def format(self):
        return self._date.strftime("%d/%m/%Y")
