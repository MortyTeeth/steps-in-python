def change_num(n):
    k = []
    z = ''
    s = str(n)
    if len(s) <= 3:
        return s
    else:
        l = s.split()

        for j in range(len(s)):
            k.append(l[0][j])
        k = k[::-1]
        for i in range(3, len(s), 3):
            k[i] += ','
        p = k[::-1]
        for n in range(len(p)):
            z += p[n]
        return z


num = int(input())

print(change_num(num))