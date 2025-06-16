list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0

for i in range(len(list1)):
    for j in range(len(list1[i])):
        if list1[i][j] > maximum:
            maximum = list1[i][j]
        else:
            maximum = maximum

print(maximum)