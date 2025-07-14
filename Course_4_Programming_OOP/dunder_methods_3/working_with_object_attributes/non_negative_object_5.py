class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        super().__setattr__(key, value)
