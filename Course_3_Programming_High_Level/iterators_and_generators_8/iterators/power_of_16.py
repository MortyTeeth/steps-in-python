class PowerOf:
    def __init__(self, number, iterator=0):
        self.number = number
        self.iterator = iterator

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number ** self.iterator
        self.iterator += 1
        return result
