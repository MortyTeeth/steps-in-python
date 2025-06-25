def excellent_students(n_o_c):
    main_list = []
    for students_and_marks in range(n_o_c):
        number_of_students_in_class = int(input())
        vr_dict = dict()
        for k in range(number_of_students_in_class):
            last_name_and_mark = input().split()
            vr_dict.update({last_name_and_mark[0]: int(last_name_and_mark[1])})
        main_list.append(vr_dict)

    final_result = []

    for students_and_marks in main_list:
        result = any(map(lambda key: True if students_and_marks[key] == 5 else False, students_and_marks))
        final_result.append(result)
    if all(final_result):
        return 'YES'
    else:
        return 'NO'


number_of_classes = int(input())
print(excellent_students(number_of_classes))
