import sys
from functools import lru_cache


@lru_cache
def just_dima():
    data = [i for i in sys.stdin]
    for word in data:
        print(''.join(sorted(word.strip())))


just_dima()
