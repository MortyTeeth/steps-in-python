class Todo:
    def __init__(self, things=None):
        self.things = []

    def add(self, case_title, priority):
        self.things.append((case_title, priority))

    def get_by_priority(self, n):
        if len(self.things) < 1:
            return []

        return [i[0] for i in self.things if i[1] == n]

    def get_low_priority(self):
        if len(self.things) < 1:
            return []
        min_priority = min([i[1] for i in self.things])
        return [i[0] for i in self.things if i[1] == min_priority]

    def get_high_priority(self):
        if len(self.things) < 1:
            return []

        max_priority = max([i[1] for i in self.things])
        return [i[0] for i in self.things if i[1] == max_priority]
