def n_m(n):
    a = []
    b = []

    sum = 0

    for i in range(n):
        l = []
        for j in range(1):
            l.append(input().split())
        a.extend(l)

    for j in range(0, len(a), 1):
        sum += int(a[j][j])
    print(sum)


n = int(input())

n_m(n)
