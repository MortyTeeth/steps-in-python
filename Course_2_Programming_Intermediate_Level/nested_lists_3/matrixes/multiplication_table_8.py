def multiplication_table(number_of_lines, number_of_columns):
    for i in range(number_of_lines):
        for j in range(number_of_columns):
            a = i * j
            if j == number_of_columns - 1:
                print(str(a), end='')
            else:
                print(str(a).ljust(3), end='')
        print()


n = int(input())
m = int(input())

multiplication_table(n, m)
