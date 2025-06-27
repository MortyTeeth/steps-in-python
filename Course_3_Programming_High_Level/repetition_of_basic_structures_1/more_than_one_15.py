def more_then_one(l):
    first_dict = {}
    for num in l:
        if num not in first_dict:
            first_dict.update({num: 1})
        else:
            first_dict.update({num: first_dict[num] + 1})

    second_dict = {i: first_dict[i] for i in first_dict if first_dict[i] > 1}
    print(*sorted(second_dict))


line = [int(i) for i in input().split()]
more_then_one(line)
