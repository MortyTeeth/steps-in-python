def filling_2(size):
    lines = int(size[0])
    columns = int(size[1])
    count = 0
    sec_count = 0

    sec_matrix = []
    main_matrix = []

    for i in range(columns):
        sec_count = count
        matrix = []
        for k in range(1, lines + 1):
            matrix.append((k + sec_count))
            count += 1
        sec_matrix.append(matrix)

    for l in range(lines):
        pre_main_matrix = []
        for m in range(columns):
            pre_main_matrix.append(str(sec_matrix[m][l]).ljust(2))
        print(*pre_main_matrix)
    print()


size = input().split()

filling_2(size)
