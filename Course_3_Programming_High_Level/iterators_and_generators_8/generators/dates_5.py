from datetime import *


def dates(start, count=None):
    try:
        if count == None:
            while True:
                yield start
                start += timedelta(1)
        else:
            for i in range(count):
                yield start + timedelta(i)
    except:
        pass
