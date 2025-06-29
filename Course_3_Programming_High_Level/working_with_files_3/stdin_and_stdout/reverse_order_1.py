import sys


def reverse_order():
    data = [line.strip() for line in sys.stdin]
    for line in data:
        print(line[::-1])


reverse_order()
