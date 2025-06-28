from datetime import date, datetime, timedelta


def neighboring_dates(string):
    list_with_difference = []
    for d in range(len(string) - 1):
        delta = abs(string[d] - string[d + 1])
        list_with_difference.append(delta.days)
    print(list_with_difference)


string_with_dates = [datetime.strptime(i, '%d.%m.%Y') for i in input().split(' ')]

neighboring_dates(string_with_dates)
