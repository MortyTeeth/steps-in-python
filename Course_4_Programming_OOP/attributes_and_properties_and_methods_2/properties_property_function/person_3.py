class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + ' ' + self.surname

    def set_fullname(self, new_name):
        self.name, self.surname = new_name.split()

    fullname = property(get_fullname, set_fullname)
