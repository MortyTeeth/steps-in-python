from datetime import date, timedelta


def num_of_sundays(year):
    first_date = date(year=year, day=1, month=1)
    second_date = date(year=year + 1, day=1, month=1)
    first_date_days = first_date.toordinal()
    second_date_days = second_date.toordinal()
    count = 0

    for d in range(first_date_days, second_date_days):
        if date.fromordinal(d).isoweekday() == 7:
            count += 1
    return count
