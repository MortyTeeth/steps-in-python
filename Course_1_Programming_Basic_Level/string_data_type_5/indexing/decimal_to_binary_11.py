num = int(input())

txt = 0

dv = ''

for i in range(1, num + 1):
    if num % 2 == 1:
        txt = 1
        dv = str(txt) + dv
        num //= 2
        if num == 0:
            break
    else:
        txt = 0
        dv = str(txt) + dv
        num //= 2
        if num == 0:
            break
print(dv)