def max_group(n_n):
    list_for_edit = [int(i) for i in range(1, n_n + 1)]
    dictionary = dict()
    for num in list_for_edit:
        vr = sum([int(i) for i in str(num)])
        if vr not in dictionary:
            dictionary.update({vr: 1})
        else:
            dictionary.update({vr: dictionary[vr] + 1})

    print(max(dictionary.values()))


natural_num = int(input())

max_group(natural_num)
