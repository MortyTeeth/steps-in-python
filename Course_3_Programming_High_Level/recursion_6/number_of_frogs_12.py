def number_of_frogs(year):
    frogs_in_first_year = 77
    if year == 1:
        return frogs_in_first_year
    else:
        return 3 * (number_of_frogs(year - 1) - 30)
