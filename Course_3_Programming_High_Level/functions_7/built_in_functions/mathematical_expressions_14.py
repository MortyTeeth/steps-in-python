import sys


def mathematical_expressions():
    data = [eval(i) for i in sys.stdin]
    print(max(data))


mathematical_expressions()
