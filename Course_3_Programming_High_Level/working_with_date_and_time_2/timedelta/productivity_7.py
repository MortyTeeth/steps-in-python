from datetime import datetime, timedelta, date


def productivity(d):
    count = 0
    for i in range(1, 10 + 1):
        print((date.fromordinal(d.toordinal() + count)).strftime('%d.%m.%Y'))
        count += i + 1


d = datetime.strptime(input(), '%d.%m.%Y')
productivity(d)
