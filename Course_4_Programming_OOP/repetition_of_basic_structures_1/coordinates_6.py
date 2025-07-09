import sys


def coordinates():
    x_y = [i for i in sys.stdin]
    for i in x_y:
        x, y = list(eval(i))
        if -90 <= x <= 90 and -180 <= y <= 180:
            print(True)
        else:
            print(False)


coordinates()
