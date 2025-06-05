num = int(input())
secnum = 0

while num != 0:
    if num != 0 and num // 10 > 0:
        secnum = num % 10
    num = num // 10
print(secnum)