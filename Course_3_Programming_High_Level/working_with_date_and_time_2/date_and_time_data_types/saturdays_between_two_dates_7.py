from datetime import date


def saturdays_between_two_dates(start, end):
    first_num = start.toordinal()
    second_num = end.toordinal()
    count = 0
    if start < end:
        for i in range(first_num, second_num + 1):
            a = date.fromordinal(i)
            if a.isoweekday() == 6:
                count += 1
        return count
    else:
        for i in range(second_num, first_num + 1):
            a = date.fromordinal(i)
            if a.isoweekday() == 6:
                count += 1
        return count
