num = int(input())

for i in range(1, num + 1):
    if 4 < i <= 9 or 16 < i <= 37 or 77 < i <= 87:
        continue
    else:
        print(i)