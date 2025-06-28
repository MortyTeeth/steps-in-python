from datetime import datetime
import calendar


def day_of_the_week(d):
    dict_with_day_name = {}
    for i in range(1, 8):
        dict_with_day_name.update({calendar.day_name[i - 1]: i - 1})
    day_of_week = d.weekday()

    for key, value in dict_with_day_name.items():
        if day_of_week == value:
            print(key)


d = datetime.strptime(input(), '%Y-%m-%d')

day_of_the_week(d)
