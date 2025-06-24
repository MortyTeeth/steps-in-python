def computer_science_lesson(f_l, s_l, t_l):
    first_set = set(f_l)
    second_set = set(s_l)
    third_set = set(t_l)

    pre_final_set = (first_set & second_set) - third_set

    converter = list(pre_final_set)

    converter_2 = []

    for i in range(len(converter)):
        converter_2.append(int(converter[i]))

    print(*reversed(sorted(converter_2)))


first_list = input().split()
second_list = input().split()
third_list = input().split()

computer_science_lesson(first_list, second_list, third_list)