col = int(input())

l = []

l2 = []

for i in range(col):
    st = input()
    l.append(st)

search = input()
a = search.lower()

for j in range(col):
    if a in l[j].lower():
        l2.append(l[j])
print(*l2, sep='\n')