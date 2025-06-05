a = int(input())

n = 0

while a < 6 and a > 0:
    if a == 5:
        n = n + 1
        a = int(input())
    elif a == 1 or a == 2 or a == 3 or a == 4:
        a = int(input())
print(n) 