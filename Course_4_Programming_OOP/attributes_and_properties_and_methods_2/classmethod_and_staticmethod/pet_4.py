class Pet:
    pets = []
    count = 0

    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)
        Pet.count += 1

    @classmethod
    def first_pet(cls):
        if len(Pet.pets) < 1:
            return None
        else:
            return cls.pets[0]

    @classmethod
    def last_pet(cls):
        if len(Pet.pets) < 1:
            return None
        else:
            return cls.pets[-1]

    @classmethod
    def num_of_pets(cls):
        return cls.count
