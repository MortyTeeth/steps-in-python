def general_figures(num):
    list_of_sets = []
    l = set()
    for i in range(num):
        str = input()
        se = set(str)

        list_of_sets.append(se)

    for k in range(num):
        list_of_sets[0].intersection_update(list_of_sets[k])

    print(*sorted(list_of_sets[0]))


number = int(input())

general_figures(number)