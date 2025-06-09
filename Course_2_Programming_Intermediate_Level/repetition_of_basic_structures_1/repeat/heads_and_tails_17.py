def shift_1(m):
    s = []
    l = []

    for i in range(len(m)):
        s.append(m[i])
    a = m.split('О')

    for j in range(len(a)):
        l.append(int(len(a[j])))

    return max(l)


mas = input()

print(shift_1(mas))