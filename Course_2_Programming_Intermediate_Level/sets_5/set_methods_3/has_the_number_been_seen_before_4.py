def has_the_number_been_seen_before(num):
    new_split = []
    split = []

    for i in range(len(num)):
        new_split.append(int(num[i]))

    for k in range(len(new_split)):
        if new_split[k] not in split:
            split.append(new_split[k])
            print('NO')
        else:
            print('YES')


numbers = input().split()

has_the_number_been_seen_before(numbers)