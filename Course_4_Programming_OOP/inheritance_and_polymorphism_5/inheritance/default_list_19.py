from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        self.default = default
        super().__init__(i for i in iterable)

    def __getitem__(self, key):
        try:
            return self.data[key]
        except:
            return self.default
