def more_than_the_previous_one(m):
    l = []
    count = 0
    for i in range(len(m)):
        l.append(int(m[i]))
    for j in range(len(l) - 1):
        if l[j] < l[j + 1]:
            count += 1
    return count

mas = input().split()

print(more_than_the_previous_one(mas))