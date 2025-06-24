def all_numbers(f_l, s_l):
    first_set = set(f_l)
    second_set = set(s_l)

    if second_set.issubset(first_set):
        print('YES')
    else:
        print('NO')


first_line = input()
second_line = input()

all_numbers(first_line, second_line)