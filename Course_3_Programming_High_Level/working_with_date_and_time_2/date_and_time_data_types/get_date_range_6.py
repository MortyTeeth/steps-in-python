from datetime import date


def get_date_range(start, end):
    if start > end:
        return []
    else:
        list_with_date = []
        first_num = start.toordinal()
        second_num = end.toordinal()
        for i in range(first_num, second_num + 1, 1):
            a = date.fromordinal(i)
            list_with_date.append(a)
        return list_with_date
