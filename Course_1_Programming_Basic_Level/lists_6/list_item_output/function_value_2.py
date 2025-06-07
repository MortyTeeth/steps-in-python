col = int(input())

sp1 = []

x = 0

for i in range(col):
    num = int(input())
    sp1.append(num)
print(*sp1, sep = '\n')
print()
for j in range(1, col + 1):
    x = sp1[j - 1] ** 2 + sp1[j - 1] * 2 + 1
    print(x, sep = '\n')