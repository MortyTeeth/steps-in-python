class Suppress:
    def __init__(self, *args):
        self.exceptions = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and isinstance(exc_val, self.exceptions):
            self.exception = exc_val
            return True
        return False
