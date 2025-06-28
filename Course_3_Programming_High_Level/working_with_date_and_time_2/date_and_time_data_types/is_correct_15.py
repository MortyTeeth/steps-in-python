from datetime import date


def is_correct(day=None, month=None, year=None):
    try:
        if day == None or month == None or year == None:
            return False
        else:
            date(int(year), int(month), int(day))
            return True
    except ValueError:
        return False
