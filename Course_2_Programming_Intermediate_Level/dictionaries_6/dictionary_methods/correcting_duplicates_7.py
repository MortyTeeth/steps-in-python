def correcting_duplicates(s):
    dict_1 = {}

    for elem in s:
        if elem not in dict_1:
            dict_1[elem] = 0
            if dict_1[elem] == 0:
                print(elem, sep='', end=' ')
            else:
                print(elem, dict_1[elem], sep='_', end=' ')
        else:
            dict_1[elem] += 1
            print(elem, dict_1[elem], sep='_', end=' ')


stroka = input().split()

correcting_duplicates(stroka)
