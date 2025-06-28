import calendar


def calender_on_month(m):
    year, month = m.split(' ')
    english_names = {}
    for i in range(len(calendar.month_abbr)):
        english_names.update({calendar.month_abbr[i]: i})
    for key, value in english_names.items():
        if key == month:
            print(calendar.month(int(year), value))


m = input()

calender_on_month(m)
