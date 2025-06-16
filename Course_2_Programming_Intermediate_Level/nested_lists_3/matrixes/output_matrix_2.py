def n_m(n, m):
    a = []
    b = []

    for i in range(n):
        l = []
        for j in range(m):
            l.append(input())
        a.append(l)
    for i in a:
        print(*i)
    print()
    for i in range(m):
        l = []
        for j in range(n):
            l.append(a[j][i])
        b.append(l)
    for i in b:
        print(*i)


n = int(input())
m = int(input())

n_m(n, m)
