import calendar


def leap_year(c_y):
    list_with_dates = []
    for i in range(c_y):
        d = int(input())
        list_with_dates.append(d)

    for y in list_with_dates:
        print(calendar.isleap(y))


count_years = int(input())

leap_year(count_years)
