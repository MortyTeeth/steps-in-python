from enum import IntEnum
from datetime import date, timedelta


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(self, today, weekday, considering_today=False):
        self.today = date(year=today.year, month=today.month, day=today.day)
        self.weekday = weekday
        self.considering_today = considering_today

    def date(self):
        return self.today + timedelta(days=self.days_until())

    def days_until(self):
        today_weekday = self.today.weekday()
        delta_days = (self.weekday - today_weekday) % 7
        if delta_days == 0 and not self.considering_today:
            delta_days = 7
        return delta_days
