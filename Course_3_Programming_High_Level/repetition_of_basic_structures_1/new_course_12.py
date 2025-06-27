def new_course(d_1, d_2, d_3):
    first_list_for_min = [d_1, d_2, d_3]
    first_min = min(first_list_for_min)
    first_list_for_min.remove(first_min)
    second_min = min(first_list_for_min)
    if (first_min + second_min) * 2 < d_1 + d_2 + d_3:
        return (first_min + second_min) * 2
    else:
        return sum([d_1, d_2, d_3])


d1, d2, d3 = int(input()), int(input()), int(input())

print(new_course(d1, d2, d3))
