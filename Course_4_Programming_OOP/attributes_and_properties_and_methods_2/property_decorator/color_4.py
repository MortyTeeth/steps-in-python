class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode
        self.r = int(self._hexcode[:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:], 16)

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(self._hexcode[:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:], 16)
