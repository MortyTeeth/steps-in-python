from datetime import date, datetime, timedelta


def fill_up_missing_dates(dates):
    real_dates = [datetime.strptime(i, '%d.%m.%Y') for i in dates]

    new_list_with_all_dates_between_max_and_min = []

    min_date = min(real_dates)
    max_date = max(real_dates)

    min_date_day = min_date.toordinal()
    max_date_day = max_date.toordinal()

    for day in range(min_date_day, max_date_day + 1):
        new_list_with_all_dates_between_max_and_min.append(date.fromordinal(day).strftime('%d.%m.%Y'))

    return new_list_with_all_dates_between_max_and_min
