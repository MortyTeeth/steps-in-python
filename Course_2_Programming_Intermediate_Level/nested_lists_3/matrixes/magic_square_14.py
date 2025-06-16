def magic_cobe(size_matrix):
    all_numbers = []
    for t in range(1, size_matrix * size_matrix + 1):
        all_numbers.append(t)

    matrix = []
    second_matrix = []
    main_dig = []
    second_dig = []
    count = 0
    count_2 = 0
    for i in range(size_matrix):
        line = input().split()
        mat = []
        for n in range(len(line)):
            mat.append(int(line[n]))
        matrix.append(mat)

        for j in range(size_matrix):
            if i + j + 1 == size_matrix:
                second_dig.append(matrix[i][j])

    for k in range(size_matrix):
        vr_mas = []
        for l in range(size_matrix):
            vr_mas.append(matrix[l][k])
        second_matrix.append(vr_mas)

    for m in range(size_matrix):
        main_dig.append(matrix[m][m])

    for o in range(size_matrix):
        if sum(matrix[o - 1]) == sum(matrix[o]):
            count = count
        else:
            count += 1

    for p in range(size_matrix):
        if sum(second_matrix[p - 1]) == sum(second_matrix[p]):
            count = count
        else:
            count += 1

    if sum(main_dig) == sum(second_dig):
        count = count
    else:
        count += 1

    for r in range(size_matrix):
        for s in range(size_matrix):
            if second_matrix[r][s] in second_matrix:
                count += 1
            else:
                count = count

    for x in range(size_matrix):
        for y in range(size_matrix):
            if matrix[x][y] in all_numbers and matrix[x][y] != matrix[x - 1][y - 1] and matrix[x][y] != matrix[y - 1][
                x - 1] and matrix[x - 1][y] != matrix[x][y - 1]:
                count_2 += 1

    if count == 0 and count_2 == len(all_numbers):
        return 'YES'
    else:
        return 'NO'


size_matrix = int(input())

print(magic_cobe(size_matrix))
