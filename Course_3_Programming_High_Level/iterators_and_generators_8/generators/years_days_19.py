import datetime
from datetime import date


def years_days(year):
    first_day = date(year=year, month=1, day=1).toordinal()
    last_day = date(year=year, month=12, day=31).toordinal()
    days = (i for i in range(first_day, last_day + 1))
    for i in days:
        yield datetime.date.fromordinal(i)
