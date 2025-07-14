class Filter:
    def __init__(self, predicate):
        self.predicate = predicate if predicate is not None else bool

    def __call__(self, iterable):
        return [i for i in iterable if self.predicate(i)]
