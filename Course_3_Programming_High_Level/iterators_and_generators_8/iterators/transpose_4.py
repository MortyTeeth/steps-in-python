def transpose(matrix):
    matrix = list(zip(*matrix))
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(i))

    return new_matrix
