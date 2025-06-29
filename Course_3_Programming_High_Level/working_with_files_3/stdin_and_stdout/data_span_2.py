import sys
from datetime import datetime


def data_span():
    data = [datetime.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin]
    min_date = min(data)
    max_date = max(data)
    delta = (max_date - min_date).days
    print(delta)


data_span()
