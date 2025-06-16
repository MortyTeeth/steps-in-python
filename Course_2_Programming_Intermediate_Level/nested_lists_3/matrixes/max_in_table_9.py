def maximum_in_table(number_of_lines, number_of_columns):
    general_list = []
    max_number = - 1000
    position_of_lines = 0
    position_of_columns = 0

    for i in range(number_of_lines):
        line_with_numbers = input().split()
        general_list.append(line_with_numbers)

    for k in range(number_of_lines):
        for l in range(number_of_columns):
            if int(general_list[k][l]) > max_number:
                max_number = int(general_list[k][l])
                position_of_lines = k
                position_of_columns = l

    print(position_of_lines, position_of_columns)


n = int(input())
m = int(input())

maximum_in_table(n, m)
