from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
         date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
         date(1666, 6, 6), date(1968, 5, 26)]

month_to_quarter = {
    1: 1, 2: 1, 3: 1,
    4: 2, 5: 2, 6: 2,
    7: 3, 8: 3, 9: 3,
    10: 4, 11: 4, 12: 4
}

for date in dates:
    quarter = month_to_quarter[date.month]
    print(f'{date.year}-Q{quarter}')