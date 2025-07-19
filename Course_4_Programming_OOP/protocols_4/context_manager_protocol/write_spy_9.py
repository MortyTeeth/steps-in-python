class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def write(self, text):
        if not self.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file2.write(text)
        self.file1.write(text)

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        else:
            if self.file1.writable() and self.file2.writable():
                return True
            else:
                return False

    def closed(self):
        if self.file1.closed and self.file2.closed:
            return True
        else:
            return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close == True:
            self.file1.close()
            self.file2.close()
        else:
            pass
