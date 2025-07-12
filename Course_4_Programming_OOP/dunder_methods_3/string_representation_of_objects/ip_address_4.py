from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register
    def _(self, ipaddress: tuple):
        self.ipaddress = '.'.join([str(i) for i in ipaddress])

    @__init__.register
    def _(self, ipaddress: list):
        self.ipaddress = '.'.join([str(i) for i in ipaddress])

    def __str__(self):
        return f"{self.ipaddress}"

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"
