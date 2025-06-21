numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
a = list(numbers)
s = 0

for i in range(len(numbers)):
    s += a[i] ** 2
print(s)