sum = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        sum += n
    else:
        sum = sum
if sum == 0:
    print(0)
else:
    print(sum)