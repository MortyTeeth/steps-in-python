class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = self.price * self.quantity

    def __getattribute__(self, name):
        if name == 'price':
            return object.__getattribute__(self, name)
        elif name == 'quantity':
            return object.__getattribute__(self, name)
        elif name == 'total':
            return object.__getattribute__(self, name)
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return self.__dict__[name]
