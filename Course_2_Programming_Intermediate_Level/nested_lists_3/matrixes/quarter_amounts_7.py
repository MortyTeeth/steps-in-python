def sums_of_quarters(size_matrix):
    array_of_all_values = []
    upper_quarter = []
    right_quarter = []
    lower_quarter = []
    left_quarter = []

    for i in range(size_matrix):

        array_of_all_values.append(input().split())

        for k in range(0, size_matrix):
            if i < k and i < size_matrix - 1 - k:
                upper_quarter.append(int(array_of_all_values[i][k]))

        for l in range(0, size_matrix):
            if i < l and i > size_matrix - 1 - l:
                right_quarter.append(int(array_of_all_values[i][l]))

        for m in range(0, size_matrix):
            if i > m and i > size_matrix - 1 - m:
                lower_quarter.append(int(array_of_all_values[i][m]))

        for n in range(0, size_matrix):
            if i > n and i < size_matrix - 1 - n:
                left_quarter.append(int(array_of_all_values[i][n]))

    print('Верхняя четверть:', sum(upper_quarter))
    print('Правая четверть:', sum(right_quarter))
    print('Нижняя четверть:', sum(lower_quarter))
    print('Левая четверть:', sum(left_quarter))


size_matrix = int(input())

sums_of_quarters(size_matrix)
