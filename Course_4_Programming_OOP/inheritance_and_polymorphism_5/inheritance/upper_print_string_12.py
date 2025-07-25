class UpperPrintString(str):
    def __init__(self, string):
        self._upper_string = super().__str__().upper()

    def __str__(self):
        return f"{self._upper_string}"
