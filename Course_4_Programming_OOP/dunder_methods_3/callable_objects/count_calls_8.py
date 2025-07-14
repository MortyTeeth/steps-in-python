class CountCalls:
    def __init__(self, func, calls=0):
        self.calls = calls
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)
