def symmetric_matrix(size_matrix):
    flag = False
    matrix = []
    count = 0
    for i in range(size_matrix):
        stroka = input().split()
        matrix.append(stroka)

    for g in range(size_matrix):
        for h in range(size_matrix):
            if matrix[g][h] == matrix[h][g]:
                flag = True
            else:
                count += 1

    if flag == True and count == 0:
        print('YES')
    else:
        print('NO')

size_matrix = int(input())

symmetric_matrix(size_matrix)