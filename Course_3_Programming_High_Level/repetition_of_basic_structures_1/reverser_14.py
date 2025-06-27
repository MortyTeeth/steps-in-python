n, x, y, a, b = [int(i) for i in input().split()]
lst = list(range(1, n + 1))

lst[x - 1:y] = lst[x - 1:y][::-1]
lst[a - 1:b] = lst[a - 1:b][::-1]
print(*lst)
