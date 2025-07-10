class Scales:
    def __init__(self):
        self.right_weight = 0
        self.left_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def get_result(self):
        if self.left_weight == self.right_weight:
            return 'Весы в равновесии'

        elif self.left_weight > self.right_weight:
            return 'Левая чаша тяжелее'

        else:
            return 'Правая чаша тяжелее'
