import sys


def commentator():
    data = [line.strip() for line in sys.stdin.readlines()]
    counter = 0
    for line in range(len(data)):
        if data[line][0] == '#' and all(not char.isdigit() for char in data[line]):
            counter += 1
    print(counter)


commentator()
