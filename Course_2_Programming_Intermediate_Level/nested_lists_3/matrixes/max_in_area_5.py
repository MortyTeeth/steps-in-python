def n_m(n):
    a = []
    l = []
    b = []

    for i in range(n):

        l.append(input().split())
        c = []
        for z in range(n):
            c.append(int(l[i][z]))
        a.append(c)

        for k in range(0, n):
            if i >= k:
                b.append(int(l[i][k]))
    print(max(b))


n = int(input())

n_m(n)
