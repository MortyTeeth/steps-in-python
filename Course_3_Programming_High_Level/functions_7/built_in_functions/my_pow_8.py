def my_pow(number):
    list_with_pair = []
    for pair in enumerate(str(number), 1):
        list_with_pair.append(pair)

    return sum([int(i[1]) ** i[0] for i in list_with_pair])
