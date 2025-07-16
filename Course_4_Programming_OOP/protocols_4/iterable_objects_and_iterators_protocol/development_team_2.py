class DevelopmentTeam:
    def __init__(self):
        self.team = list()

    def add_junior(self, *args):
        for i in args:
            self.team.append((i, 'junior'))

    def add_senior(self, *args):
        for i in args:
            self.team.append((i, 'senior'))

    def __iter__(self):
        self.team = sorted(self.team, key=lambda x: x[1])
        yield from self.team
