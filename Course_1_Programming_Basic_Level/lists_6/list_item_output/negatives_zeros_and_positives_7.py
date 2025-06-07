col = int(input())

l1 = []
l2 = []
l3 = []

for i in range(col):
    num = int(input())
    if num < 0:
        l1.append(num)
    elif num == 0:
        l2.append(num)
    else:
        l3.append(num)
l1.extend(l2)
l1.extend(l3)
print(*l1, sep = '\n')