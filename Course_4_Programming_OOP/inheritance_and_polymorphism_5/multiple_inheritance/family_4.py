class Father:
    def __init__(self, mood="neutral"):
        self.mood = mood

    def greet(self):
        return f"Hello!"

    def be_strict(self):
        self.mood = "strict"


class Mother:
    def __init__(self, mood="neutral"):
        self.mood = mood

    def greet(self):
        return f"Hi, honey!"

    def be_kind(self):
        self.mood = "kind"


class Daughter(Mother, Father):
    pass


class Son(Father, Mother):
    pass
