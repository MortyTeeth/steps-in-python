def tribonacci_sequence(num):
    tr = [1, 1, 1]

    if num > 3:
        for i in range(3, num):
            tr.append(tr[i - 3] + tr[i - 2] + tr[i - 1])
        print(*tr)
    elif num == 1:
        print(1)
    elif num == 2:
        print(1, 1)
    elif num == 3:
        print(1, 1, 1)


num = int(input())

tribonacci_sequence(num)
