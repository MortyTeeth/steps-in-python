class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self._matrix = [[value for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join(' '.join(str(el) for el in row) for row in self._matrix)

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __pos__(self):
        new = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new._matrix[i][j] = +self._matrix[i][j]
        return new

    def __neg__(self):
        new = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new._matrix[i][j] = -self._matrix[i][j]
        return new

    def __invert__(self):
        new = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new._matrix[j][i] = self._matrix[i][j]
        return new

    def __round__(self, ndigits=None):
        new = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new._matrix[i][j] = round(self._matrix[i][j], ndigits)
        return new
