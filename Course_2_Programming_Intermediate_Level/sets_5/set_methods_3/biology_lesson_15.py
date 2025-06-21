def biology_lesson(f_l, s_l, t_l):
    set_1 = set(f_l)
    set_2 = set(s_l)
    set_3 = set(t_l)
    set_4 = set(range(11))

    pre_final_set = (set_1 | set_2 | set_3)
    converter = list(pre_final_set)
    converter_2 = []

    for i in range(len(converter)):
        converter_2.append(int(converter[i]))
    converter_3 = set(converter_2)

    final_set = set_4 - converter_3

    print(*sorted(final_set))


first_line = input().split()
second_line = input().split()
third_line = input().split()

biology_lesson(first_line, second_line, third_line)
