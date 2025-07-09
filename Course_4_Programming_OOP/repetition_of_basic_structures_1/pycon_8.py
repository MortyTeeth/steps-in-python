from datetime import date
import calendar


def pycon(y, m):
    first_date = date(year=y, month=m, day=1).toordinal()
    _, last_day = calendar.monthrange(y, m)
    second_date = date(year=y, month=m, day=last_day).toordinal()
    count = 0
    for i in range(first_date, second_date):
        dat = date.fromordinal(i)
        if dat.isoweekday() == 4:
            count += 1
            if count == 4:
                print(date.fromordinal(i).strftime('%d.%m.%Y'))
                break


year, month = int(input()), int(input())

pycon(year, month)
