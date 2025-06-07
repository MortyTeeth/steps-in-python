num = int(input())

spisok = [i ** 2 for i in range(1, num + 1)]

print(*spisok, sep = '\n')