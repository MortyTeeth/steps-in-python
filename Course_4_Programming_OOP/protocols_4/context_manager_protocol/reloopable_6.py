class Reloopable:
    def __init__(self, file):
        self.file = list(file)
        self.f = file

    def __enter__(self):
        try:
            return self.file
        except:
            with self.f:
                return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

    def __iter__(self):
        return iter(self.file)
