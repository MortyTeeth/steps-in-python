n = int(input())

m = 0
pm = 0

realm = 0
realpm = 0


for i in range(n):
    a = int(input())
    if a > m:
        m, pm = a, m
        if m > pm:
            realm = m
            realpm = pm
        else:
            realm = m
            realpm = a
    elif a < m:
        if a < pm:
            if m > pm:
                realm = m
                realpm = pm
            else:
                realm = pm
                realpm = m
        else:
            realm = m
            realpm = a
print(realm)
print(realpm)
