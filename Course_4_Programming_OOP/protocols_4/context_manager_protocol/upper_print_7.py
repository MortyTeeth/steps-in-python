class UpperPrint:
    def __init__(self):
        pass

    def __enter__(self):
        import sys
        self.sys = sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        self.sys.stdout.write = self.original_write
