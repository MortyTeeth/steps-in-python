class LowerString(str):
    def __new__(cls, *args, **kwargs):
        obj = str(*args, **kwargs).lower()
        return super().__new__(cls, obj)

    def __str__(self):
        return super().__str__()
