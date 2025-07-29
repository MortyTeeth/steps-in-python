class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.price}$"


class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(int(str(item).split(",")[1][1:-1]) for item in self.items)

    def remove(self, item):
        self.new_items = []
        for i in self.items:
            if item in str(i):
                pass
            else:
                self.new_items.append(i)

        self.items = self.new_items

    def __str__(self):
        return '\n'.join([str(item) for item in self.items])
