def same_numbers(f_l, s_l):
    first_num = int(f_l)
    second_num = int(s_l)
    count = 0
    for i in range(len(f_l)):
        for k in range(len(s_l)):
            if f_l[i] == s_l[k]:
                count += 1

    if count > 0:
        print('YES')
    else:
        print('NO')


first_line = input()

second_line = input()

same_numbers(first_line, second_line)