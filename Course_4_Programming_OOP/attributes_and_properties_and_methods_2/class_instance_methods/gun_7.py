from itertools import cycle


class Gun:
    def __init__(self):
        self.count = 0
        self.iterator = cycle(['pif', 'paf'])

    def shoot(self):
        print(next(self.iterator))
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0
        self.iterator = cycle(['pif', 'paf'])
