class SequenceZip:
    def __init__(self, *args):
        self.args = list(zip(*args))

    def __len__(self):
        return len(self.args)

    def __iter__(self):
        return iter(self.args)

    def __getitem__(self, key):
        return self.args[key]

    def __setitem__(self, key, value):
        self.args[key] = value
        return self.args[key]
