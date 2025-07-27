def get_method_owner(cls, method):
    for i in cls.mro():
        if method in i.__dict__:
            return i
    else:
        return None
