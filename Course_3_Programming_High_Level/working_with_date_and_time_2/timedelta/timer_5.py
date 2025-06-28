from datetime import datetime, timedelta


def timer(t, seconds):
    delta = t + timedelta(seconds=seconds)
    return delta.time()


t = datetime.strptime(input(), '%H:%M:%S')
sec = int(input())

print(timer(t, sec))
