def addition_matrix(matrix_size):
    lines = int(matrix_size[0])
    columns = int(matrix_size[1])
    first_matrix = []
    second_matrix = []
    for i in range(lines):
        line = input().split()
        first_matrix.append(line)

    strange_line = input()

    for k in range(lines):
        line = input().split()
        second_matrix.append(line)

    for l in range(lines):
        addition_matrix = []
        for m in range(columns):
            addition_matrix.append(int(first_matrix[l][m]) + int(second_matrix[l][m]))
        print(*addition_matrix)


matrix_size = input().split()

addition_matrix(matrix_size)
