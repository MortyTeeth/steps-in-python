def print_operation_table(operation, rows, cols):
    matrix = []
    for row in range(1, rows + 1):
        inside_matrix = []
        for col in range(1, cols + 1):
            inside_matrix.append(operation(row, col))
        matrix.append(inside_matrix)

    for l in matrix:
        print(*l)
