def gde_tochka(q):
    one = 0
    two = 0
    three = 0
    four = 0
    string1 = ''
    string2 = ''
    string3 = ''
    string4 = ''
    for i in range(q):
        A = input().split()
        x, y = int(A[0]), int(A[1])
        if x > 0 and y > 0:
            one += 1
        elif x > 0 and y < 0:
            four += 1
        elif x < 0 and y > 0:
            two += 1
        elif x < 0 and y < 0:
            three += 1
    string1 = 'Первая четверть: ' + str(one)
    string2 = 'Вторая четверть: ' + str(two)
    string3 = 'Третья четверть: ' + str(three)
    string4 = 'Четвертая четверть: ' + str(four)
    final = [string1, string2, string3, string4]
    return print(*final, sep='\n')


quantity_dot = int(input())

gde_tochka(quantity_dot)