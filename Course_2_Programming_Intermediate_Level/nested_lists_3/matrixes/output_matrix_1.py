def n_m(n, m):
    a = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(input())
        a.append(l)
    for i in a:
        print(*i)


n = int(input())
m = int(input())

n_m(n, m)
