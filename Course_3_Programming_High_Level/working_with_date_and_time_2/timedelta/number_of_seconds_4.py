from datetime import datetime, timedelta


def count_seconds(d):
    delta = timedelta(hours=d.hour, minutes=d.minute, seconds=d.second)
    return int(delta.total_seconds())


d = datetime.strptime(input(), '%H:%M:%S').time()

print(count_seconds(d))
