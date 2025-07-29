class Queue:
    def __init__(self, pairs=None):
        if pairs is None:
            self.pairs = {}
        elif isinstance(pairs, dict):
            self.pairs = pairs.copy()
        else:
            self.pairs = dict(pairs)

    def add(self, value):
        key, val = value
        if key in self.pairs:
            del self.pairs[key]
        self.pairs[key] = val

    def pop(self):
        if len(self.pairs) > 0:
            self.pairs = list(self.pairs.items())
            for_return = self.pairs[0]
            del self.pairs[0]
            self.pairs = dict(self.pairs)
            return for_return
        else:
            raise KeyError("Очередь пуста")

    def __str__(self):
        formatted = ', '.join(f"('{k}', {v})" for k, v in self.pairs.items())
        return f"Queue([{formatted}])"

    def __len__(self):
        return len(self.pairs)
