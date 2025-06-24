def dif(f_l, s_l):
    set_1 = set(f_l)
    set_2 = set(s_l)
    set_3 = set_1.intersection(set_2)
    print(len(set_3))


first_list = input().split()
second_list = input().split()

dif(first_list, second_list)
