num = int(input())

numeral = num % 10
count = 0

for i in range(len(str(num))):
    if num % 10 == numeral:
        count = count
        num = num // 10
    else:
        count = count + 1
        num = num // 10
if count == 0:
    print("YES")
else:
    print('NO')