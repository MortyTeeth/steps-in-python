def all_ten_num(f_l, s_l):
    f = list(f_l)
    s = list(s_l)
    f_s = f + s

    final_m = set(f_s)

    if len(final_m) == 10:
        print('YES')
    else:
        print('NO')


first_list = input()
second_list = input()

all_ten_num(first_list, second_list)