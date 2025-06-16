def pascal(l):
    lst = [[1]]
    for i in range(1, l):
        row = [1] * (i + 1)
        for j in range(i):
            if j != 0 and j != i:
                row[j] = lst[i - 1][j - 1] + lst[i - 1][j]
        lst.append(row)

    for g in range(len(lst)):
        print(*lst[g])


list_triangle = int(input())

pascal(list_triangle) 