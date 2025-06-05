num = int(input())


for i in range(1, num + 1):
    count = 0
    for k in range(1, num + 1):
        if i % k == 0:
            count += 1
    print(str(i) + count * '+')