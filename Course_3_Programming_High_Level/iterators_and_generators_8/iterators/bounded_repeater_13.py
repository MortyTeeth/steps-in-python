class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        pass

    def __iter__(self):
        return self

    def __next__(self):
        while self.times > 0:
            self.times -= 1
            return self.obj
        raise StopIteration
