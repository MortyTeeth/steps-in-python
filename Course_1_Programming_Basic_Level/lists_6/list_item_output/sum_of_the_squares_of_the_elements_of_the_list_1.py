numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
l = []

for num in numbers:
    num = num ** 2
    l.append(num)
a = sum(l)
print(a)