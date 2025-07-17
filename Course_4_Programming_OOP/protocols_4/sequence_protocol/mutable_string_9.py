class MutableString:
    def __init__(self, string=None):
        self.string = string if string is not None else ''

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"MutableString('{self.string}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()

    def __add__(self, other):
        return MutableString(self.string + other.string)

    def __getitem__(self, item):
        return MutableString(self.string[item])

    def __setitem__(self, key, value):
        self.string = list(self.string)
        self.string[key] = value
        self.string = ''.join(self.string)

    def __delitem__(self, key):
        self.string = list(self.string)
        del self.string[key]
        self.string = ''.join(self.string)
