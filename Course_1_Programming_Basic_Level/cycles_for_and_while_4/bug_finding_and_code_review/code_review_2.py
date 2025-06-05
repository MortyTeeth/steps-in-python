mx = -10000
s = 0
have = 0
for i in range(10):
    x = int(input())
    if x < 0:
        have += 1
        s += x
        if x > mx:
            mx = x
if have > 0:
    print(s)
    print(mx)
else:
    print('NO')