key_roman_arg_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class RomanNumeral:
    def __init__(self, number):
        self.roman_numeral = number

    def __int__(self):
        total = 0
        prev_value = 0
        for ch in reversed(self.roman_numeral):
            value = key_roman_arg_decimal[ch]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            total_value = int(self) + int(other)
            return RomanNumeral(RomanNumeral.to_roman(total_value))

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            total_value = int(self) - int(other)
            return RomanNumeral(RomanNumeral.to_roman(total_value))

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) > int(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) <= int(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RomanNumeral):
            return int(self) >= int(other)
        return NotImplemented

    def __str__(self):
        return self.roman_numeral

    @staticmethod
    def to_roman(number):
        roman_pieces = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]
        result = ""
        for roman, value in roman_pieces:
            while number >= value:
                result += roman
                number -= value
        return result
