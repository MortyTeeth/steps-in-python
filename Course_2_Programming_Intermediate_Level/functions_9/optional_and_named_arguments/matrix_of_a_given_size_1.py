def matrix(n=None, m=None, value=None):
    if n is None and m is None and value is None:
        matrix = [[0]]
        return matrix

    elif m is None and value is None:
        big_matrix = []
        m = n
        for i in range(n):
            matrix = []
            for k in range(m):
                matrix.append(0)
            big_matrix.append(matrix)

        return big_matrix

    elif value is None:
        big_matrix = []
        for i in range(n):
            matrix = []
            for k in range(m):
                matrix.append(0)
            big_matrix.append(matrix)
        return big_matrix
    else:
        big_matrix = []
        for i in range(n):
            matrix = []
            for k in range(m):
                matrix.append(value)
            big_matrix.append(matrix)
        return big_matrix
