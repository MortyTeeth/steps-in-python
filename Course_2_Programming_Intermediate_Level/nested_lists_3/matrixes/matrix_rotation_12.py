def rotate_the_matrix(matrix_size):
    main_mas = []

    for i in range(matrix_size):
        stroka = input().split()
        main_mas.append(stroka)

    for k in range(matrix_size):
        sec_mas = []
        third_mas = []
        for l in range(matrix_size):
            sec_mas.append(int(main_mas[l][k]))
            third_mas = sec_mas[::-1]
        print(*third_mas)


matrix_size = int(input())

rotate_the_matrix(matrix_size)
