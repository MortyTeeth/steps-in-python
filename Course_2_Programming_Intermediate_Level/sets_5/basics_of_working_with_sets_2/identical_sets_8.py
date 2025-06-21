def identical_sets(f_l, s_l):
    if set(f_l) == set(s_l):
        print('YES')
    else:
        print('NO')


first_list = input()
second_list = input()

identical_sets(first_list, second_list)
