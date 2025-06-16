def filling_4(size_matrix):
    matrix = []
    for i in range(size_matrix):
        matrix = []
        for j in range(size_matrix):
            if (i <= j and i <= size_matrix - 1 - j) or (i >= j and i >= size_matrix - 1 - j):
                if j == size_matrix - 1:
                    matrix.append('1')
                else:
                    matrix.append('1'.ljust(3))
            else:
                if j == size_matrix - 1:
                    matrix.append('0')
                else:
                    matrix.append('0'.ljust(3))
        print(*matrix)


size_matrix = int(input())

filling_4(size_matrix)
