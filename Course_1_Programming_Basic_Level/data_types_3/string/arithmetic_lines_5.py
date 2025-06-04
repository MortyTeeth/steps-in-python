a = input()
b = input()
c = input()

d = len(a)
e = len(b)
f = len(c)

if (d - e == e - f) or (d - f == d - e) or (e - d == d - f) or (e - f == f - d) or (f - d == d - e) or (f - e == e - d):
    print('YES')
else:
    print('NO')