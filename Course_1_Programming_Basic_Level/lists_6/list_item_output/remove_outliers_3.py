col = int(input())

l = []

for i in range(col):
    num = int(input())
    l.append(num)
del l[l.index(max(l))]
del l[l.index(min(l))]
l.extend
print(*l, sep='\n')