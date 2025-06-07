num = int(input())

l = []
finall = []

for i in range(1, num + 1):
    s = int(input())
    l.append(s)
for j in range(0, num - 1):
    finall.append(l[j] + l[j + 1])
print(finall)