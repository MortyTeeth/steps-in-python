def change_num(m):
    l = []
    if len(m) % 2 == 0:
        for i in range(0, len(m), 2):
            x, y = m[i + 1], m[i]
            l.append(x)
            l.append(y)
        print(*l)
    else:
        for i in range(0, len(m) - 1, 2):
            x, y = m[i + 1], m[i]
            l.append(x)
            l.append(y)
        l.append(m[-1])
        print(*l)

mas = input().split()

change_num(mas)