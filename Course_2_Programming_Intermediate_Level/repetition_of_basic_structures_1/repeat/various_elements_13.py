def shift(m):
    s = []
    l = []
    count = 0
    for i in range(len(m)):
        s.append(m[i])
    for j in range(len(s)):
        if s[j] not in l:
            l.append(s[j])

    print(len(l))


mas = input().split()

shift(mas)