def anagrams_2(f_l, s_l):
    special_symbols = '.,!?:;- '
    f_l_after_edit = ''
    s_l_after_edit = ''
    f_d = {}
    s_d = {}

    for i in range(len(f_l)):
        if f_l[i] not in special_symbols:
            f_l_after_edit += f_l[i]
    f_l_1 = f_l_after_edit.lower()

    for k in range(len(s_l)):
        if s_l[k] not in special_symbols:
            s_l_after_edit += s_l[k]
    s_l_2 = s_l_after_edit.lower()

    for char in f_l_1:
        if char not in f_d:
            f_d[char] = 1
        else:
            f_d[char] += 1

    for char_1 in s_l_2:
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

anagrams_2(first_line, second_line)
