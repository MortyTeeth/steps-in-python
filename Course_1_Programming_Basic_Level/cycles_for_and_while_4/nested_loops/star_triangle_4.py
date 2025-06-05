base = int(input())

count = 0
for i in range(1, base):
    if base - base // 2 >= i:
        count += 1
        print('*' * i)
for j in range(count + 1, base + 1):
    if base - base // 2 < j:
        count -= 1
        print('*' * (count))