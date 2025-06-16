def filling_snake(size):
    lines = int(size[0])
    columns = int(size[1])
    count = 0
    main_matrix = []

    for i in range(lines):
        sec_count = count
        matrix = []
        for k in range(1, columns + 1):
            matrix.append(k + sec_count)
            count += 1
        main_matrix.append(matrix)

    for l in range(lines):
        for m in range(columns):
            if m == columns - 1:
                if l % 2 == 0:
                    print(str(main_matrix[l][m]))
                else:
                    print(str(main_matrix[l][-(m + 1)]))
            else:
                if l % 2 == 0:
                    print(str(main_matrix[l][m]).ljust(3), end='')
                else:
                    print(str(main_matrix[l][-(m + 1)]).ljust(3), end='')


size = input().split()

filling_snake(size)
