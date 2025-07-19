class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r+', encoding='UTF-8', newline='\n')
        return self.file.read().splitlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
