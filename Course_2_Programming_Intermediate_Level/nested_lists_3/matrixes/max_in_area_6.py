def max_in_the_region(size_matrix):
    array_of_all_values = []
    first_triangle = []
    second_triangle = []

    for i in range(size_matrix):

        array_of_all_values.append(input().split())

        for k in range(0, size_matrix):
            if i <= k and i >= size_matrix - 1 - k:
                first_triangle.append(int(array_of_all_values[i][k]))

        for m in range(0, size_matrix):
            if i >= m and i <= size_matrix - 1 - m:
                second_triangle.append(int(array_of_all_values[i][m]))

    first_triangle.extend(second_triangle)
    print(max(first_triangle))


size_matrix = int(input())

max_in_the_region(size_matrix)
