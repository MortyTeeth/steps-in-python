def secondary_diagonal(matrix_size):
    for i in range(matrix_size):
        matrix = []
        for j in range(matrix_size):
            if i + j + 1 == matrix_size:
                matrix.append(1)
            elif (i >= j and i < matrix_size - 1 - j) or (i < j and i < matrix_size - 1 - j):
                matrix.append(0)
            else:
                matrix.append(2)
        print(*matrix)


matrix_size = int(input())

secondary_diagonal(matrix_size)
