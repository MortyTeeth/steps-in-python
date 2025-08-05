class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def singleton(cls):
    class WrappedSingleton(cls, Singleton):
        def __new__(cls, *args, **kwargs):
            return Singleton.__new__(cls)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    return WrappedSingleton
