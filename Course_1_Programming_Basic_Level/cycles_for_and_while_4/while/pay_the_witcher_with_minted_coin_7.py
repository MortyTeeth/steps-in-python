z = int(input())
a = 1
b = 5
c = 10
d = 25

all = 0

while z >= 25:
    all += 1
    z = z - 25
while z >= 10:
    all += 1
    z = z - 10
while z >= 5:
    all += 1
    z = z - 5
while z >= 1:
    all += 1
    z = z - 1
print(all)  