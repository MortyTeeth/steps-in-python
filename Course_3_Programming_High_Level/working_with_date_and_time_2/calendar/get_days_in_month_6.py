import calendar
from datetime import datetime


def get_days_in_month(y, m):
    list_with_date = []
    year, month = y, m
    first_d = datetime(year=year, month=datetime.strptime(month, '%B').month, day=1)
    d = datetime.strptime(str(y) + ' ' + str(m), '%Y %B')
    week_day, count_day_in_month = calendar.monthrange(d.year, d.month)
    second_d = datetime(year=year, month=datetime.strptime(month, '%B').month, day=count_day_in_month)

    first_d_day = first_d.toordinal()
    second_d_day = second_d.toordinal()

    for k in range(first_d_day, second_d_day + 1):
        list_with_date.append(datetime.fromordinal(k).date())
    return list_with_date
