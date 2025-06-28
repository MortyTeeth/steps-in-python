from datetime import datetime, timedelta, date

week = [0, 0, 0, 0, 0, 0, 0]

for year in range(1, 10000):
    for month in range(1, 13):
        week[date(year=year, month=month, day=13).weekday()] += 1
print(*week, sep='\n')
