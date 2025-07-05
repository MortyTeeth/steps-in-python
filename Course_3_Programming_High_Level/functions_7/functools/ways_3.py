from functools import lru_cache


@lru_cache
def ways(n):
    try:
        if n == 1 or n == 2 or n == 3:
            return 1
        elif n == 4:
            return 2
        else:
            return ways(n - 1) + ways(n - 3) + ways(n - 4)
    except:
        pass
