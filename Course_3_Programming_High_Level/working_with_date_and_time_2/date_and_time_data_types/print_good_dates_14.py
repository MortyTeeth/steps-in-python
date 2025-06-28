from datetime import date


def print_good_dates(dates):
    if len(dates) != 0:
        list_with_dates = []
        for dat in dates:
            if all([dat.year == 1992, dat.month + dat.day == 29]):
                list_with_dates.append(dat)

        sorted_list = sorted(list_with_dates)

        for da in sorted_list:
            print(da.strftime('%B %d, %Y'))
    else:
        print()
