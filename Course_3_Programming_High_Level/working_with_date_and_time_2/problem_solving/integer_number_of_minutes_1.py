from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

list_with_delta = []
summa = timedelta(minutes=0, hours=0, seconds=0)

for delta in data:
    su = datetime.strptime(delta[1], '%H:%M') - datetime.strptime(delta[0], '%H:%M')
    summa += su
print(int(summa.total_seconds() // 60))
