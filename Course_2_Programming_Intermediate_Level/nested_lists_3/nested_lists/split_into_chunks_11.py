def chunked(lines, num):
    main_matrix = []
    for i in range(0, len(lines), num):
        main_matrix.append(lines[i:i + num])
    print(main_matrix)


lines = input().split()
num = int(input())

chunked(lines, num)
