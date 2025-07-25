class FuzzyString(str):
    def __new__(cls, *args, **kwargs):
        obj = str(*args, **kwargs).lower()
        return super().__new__(cls, obj)

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):  # ==
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(self).lower() == str(other).lower():
            return True
        else:
            return False

    def __ne__(self, other):  # !=
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(self).lower() != str(other).lower():
            return True
        else:
            return False

    def __lt__(self, other):  # <
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(self).lower() < str(other).lower():
            return True
        else:
            return False

    def __gt__(self, other):  # >
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(self).lower() > str(other).lower():
            return True
        else:
            return False

    def __le__(self, other):  # <=
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(self).lower() <= str(other).lower():
            return True
        else:
            return False

    def __ge__(self, other):  # >=
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(self).lower() >= str(other).lower():
            return True
        else:
            return False

    def __contains__(self, other):  # other in self
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        if str(other).lower() in str(self).lower():
            return True
        else:
            return False
