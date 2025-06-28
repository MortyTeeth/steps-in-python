import calendar
from datetime import datetime


def count_days(d):
    week_day, count_day_in_month = calendar.monthrange(d.year, d.month)
    print(count_day_in_month)


d = datetime.strptime(input(), '%Y %m')

count_days(d)
