def shift(m):
    l = []
    for i in range(len(m)):
        l.append(int(m[i]))
    l.insert(0, l[len(l) - 1])
    del l[len(l) - 1]
    print(*l)


mas = input().split()

shift(mas)