def n_m(n):
    a = []
    summa = 0
    l = []

    for i in range(n):
        for j in range(1):
            l.append(input().split())
            c = []
            for hz in range(n):
                c.append(int(l[i][hz]))
            a.append(c)

    for g in range(len(a)):
        count = 0
        summa = sum(a[g])
        sr = summa / n
        for s in range(n):
            if a[g][s] > sr:
                count += 1
            else:
                count = count
        print(count)


n = int(input())

n_m(n)
