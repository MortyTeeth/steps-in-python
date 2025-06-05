n = int(input())
max_digit = -1
flag = 0
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        flag += 1
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if flag > 0:
    print(max_digit)
else:
    print('NO')