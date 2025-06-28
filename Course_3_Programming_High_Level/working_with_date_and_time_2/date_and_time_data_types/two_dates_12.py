from datetime import date


def two_date(f, s):
    if f > s:
        return s.strftime('%d-%m (%Y)')
    elif f < s:
        return f.strftime('%d-%m (%Y)')
    else:
        return f.strftime('%d-%m (%Y)')


year, month, day = input().split('-')
year2, month2, day2 = input().split('-')

first_date = date(int(year), int(month), int(day))
second_date = date(int(year2), int(month2), int(day2))

print(two_date(first_date, second_date))
