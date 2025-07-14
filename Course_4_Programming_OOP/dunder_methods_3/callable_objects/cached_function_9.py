class CachedFunction:
    def __init__(self, func):
        self.cache = dict()
        self.func = func

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        else:
            result = self.func(*args)
            self.cache[args] = result
            return result
