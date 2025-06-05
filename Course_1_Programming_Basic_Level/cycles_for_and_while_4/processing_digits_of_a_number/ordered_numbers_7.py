num = int(input())

realnum = num

count = 0

while num % 10 <= num // 10 % 10:
    num = num // 10
    count += 1
count += 1
if count == len(str(realnum)):
    print('YES')
else:
    print('NO')