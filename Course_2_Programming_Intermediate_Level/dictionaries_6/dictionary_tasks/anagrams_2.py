def anagrams_1(f_l, s_l):
    f_d = {}
    s_d = {}
    for char in f_l:
        if char not in f_d:
            f_d[char] = 1
        else:
            f_d[char] += 1

    for char_1 in s_l:
        if char_1 not in s_d:
            s_d[char_1] = 1
        else:
            s_d[char_1] += 1

    if f_d == s_d:
        print('YES')
    else:
        print('NO')


first_line = input()
second_line = input()

anagrams_1(first_line, second_line)
