class Ord:
    def __getattribute__(self, item):
        return ord(item)
