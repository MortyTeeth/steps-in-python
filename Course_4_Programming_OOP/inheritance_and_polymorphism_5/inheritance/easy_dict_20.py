class EasyDict(dict):
    def __init__(self, items=(), **kwargs):
        self.update(items)
        self.update(**kwargs)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value

    def __getattr__(self, key):
        return self[key]
