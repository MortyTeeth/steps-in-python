def generate_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = min(i, j, n - i - 1, n - j - 1) + 1
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row)


n = int(input())
result = generate_matrix(n)
print_matrix(result)
