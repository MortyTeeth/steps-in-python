from datetime import datetime, timedelta, date


def the_most_understandable_condition(start, end):
    start_days = start.toordinal()
    end_days = end.toordinal()

    list_with_date = []

    for d in range(start_days, end_days + 1):
        if (datetime.fromordinal(d).day + datetime.fromordinal(d).month) % 2 != 0:
            list_with_date.append(datetime.fromordinal(d).strftime('%d.%m.%Y'))

    real_start_days = datetime.strptime(list_with_date[0], '%d.%m.%Y').toordinal()

    for d in range(real_start_days, end_days + 1, 3):
        if datetime.fromordinal(d).isoweekday() != 1 and datetime.fromordinal(d).isoweekday() != 4:
            print(datetime.fromordinal(d).strftime('%d.%m.%Y'))


start_date = datetime.strptime(input(), '%d.%m.%Y')
end_date = datetime.strptime(input(), '%d.%m.%Y')

the_most_understandable_condition(start_date, end_date)
