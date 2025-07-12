class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = ''.join([i for i in phone_number if i != ' '])

    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

    def __repr__(self):
        return f"PhoneNumber('{''.join([i for i in self.phone_number if i != ' '])}')"
