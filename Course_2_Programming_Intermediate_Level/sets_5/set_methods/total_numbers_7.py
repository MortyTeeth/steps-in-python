def common_numbers(f_l, s_l):
    set_1 = set(f_l)
    set_2 = set(s_l)
    set_3 = set_1.intersection(set_2)
    no_set = list(set_3)
    mas = []
    for i in range(len(no_set)):
        mas.append(int(no_set[i]))
    print(*sorted(mas))


first_list = input().split()
second_list = input().split()

common_numbers(first_list, second_list)
