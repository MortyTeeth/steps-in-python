from datetime import datetime, timedelta


def previous_and_next_dates(d):
    previous_day = (d.date() - timedelta(days=1)).strftime('%d.%m.%Y')
    next_day = (d.date() + timedelta(days=1)).strftime('%d.%m.%Y')
    print(previous_day, next_day, sep='\n')


d = datetime.strptime(input(), '%d.%m.%Y')

previous_and_next_dates(d)
