def math_lesson(f_l, s_l, t_l):
    set_1 = set(f_l)
    set_2 = set(s_l)
    set_3 = set(t_l)

    pre_final_set = set_1 | set_2 | set_3
    final_set = pre_final_set - (set_1 & set_2 & set_3)
    converter = list(final_set)
    converter_2 = []

    for i in range(len(converter)):
        converter_2.append(int(converter[i]))

    print(*sorted(converter_2))


first_line = input().split()
second_line = input().split()
third_line = input().split()

math_lesson(first_line, second_line, third_line)
