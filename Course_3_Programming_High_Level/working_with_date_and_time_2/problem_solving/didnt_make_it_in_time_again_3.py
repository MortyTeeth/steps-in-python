from datetime import datetime, timedelta


def not_in_time(d):
    d_time = d.time()

    store_opening_house = {1: ['9:00', '21:00'], 2: ['9:00', '21:00'], 3: ['9:00', '21:00'], 4: ['9:00', '21:00'],
                           5: ['9:00', '21:00'], 6: ['9:00', '18:00'], 7: ['9:00', '18:00']}

    for key, value in store_opening_house.items():
        if d.isoweekday() == key:
            if d_time < datetime.strptime(value[1], '%H:%M').time() and d_time >= datetime.strptime(value[0],
                                                                                                    '%H:%M').time():
                count_hours_and_minutes = (
                            datetime.combine(d.date(), datetime.strptime(value[1], '%H:%M').time()) - timedelta(
                        hours=d.hour, minutes=d.minute)).time()
                print(count_hours_and_minutes.minute + count_hours_and_minutes.hour * 60)
            else:
                print('Магазин не работает')


d = datetime.strptime(input(), '%d.%m.%Y %H:%M')

not_in_time(d)
