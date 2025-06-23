import random

length = int(input())  # длина пароля

for i in range(length):
    a = random.randrange(1, 3)
    if a == 1:
        print((chr(random.randint(65, 90))).lower(), end='')
    else:
        print((chr(random.randint(65, 90))).upper(), end='')
