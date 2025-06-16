def filling_5(size):
    lines = int(size[0])
    columns = int(size[1])
    matrix = []

    for i in range(1, 2):
        for j in range(1, columns + 1):
            matrix.append(j)

    for k in range(lines):
        print(*matrix)
        matrix.append(matrix[0])
        matrix.remove(matrix[0])

size = input().split()

filling_5(size)