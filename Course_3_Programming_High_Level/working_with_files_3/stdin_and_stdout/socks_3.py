import sys


def socks():
    anri = 'Анри'
    dima = 'Дима'
    data = [int(i.strip()) for i in sys.stdin]

    if data[-1] % 2 == 0 and len(data) % 2 == 0:
        print(dima)
    elif data[-1] % 2 == 0 and len(data) % 2 == 1:
        print(anri)
    elif data[-1] % 2 == 1 and len(data) % 2 == 0:
        print(anri)
    else:
        print(dima)


socks()
