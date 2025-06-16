def mirror_image(matrix_size):
    main_mas = []
    reverse_mas = []
    for i in range(matrix_size):
        stroka = input().split()
        main_mas.append(stroka)

    reverse_mas = main_mas[::-1]

    for k in range(matrix_size):
        print(*reverse_mas[k])


matrix_size = int(input())

mirror_image(matrix_size)
