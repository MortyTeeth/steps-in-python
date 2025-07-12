class AnyClass:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        if len(self.kwargs) < 1:
            return f'AnyClass: '
        else:
            return f"AnyClass: {', '.join(f'{k}={v!r}' for k, v in self.kwargs.items())}"

    def __repr__(self):
        if len(self.kwargs) < 1:
            return f'AnyClass()'
        else:
            return f"AnyClass({', '.join(f'{k}={v!r}' for k, v in self.kwargs.items())})"
