class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def check_key(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key < 0 or key > len(self.sequence):
            raise IndexError
        return key

    def __getitem__(self, key):
        key = self.check_key(key)
        return list(reversed(self.sequence))[key]

    def __setitem__(self, key, value):
        key = self.check_key(key)
        self.sequence[key] = value
