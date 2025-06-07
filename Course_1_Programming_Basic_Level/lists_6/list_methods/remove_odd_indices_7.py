col = int(input())
sp1 = []
sp2 = []

for i in range(col):
    num = int(input())
    sp1.append(num)
del sp1[1::2]
print(sp1)   