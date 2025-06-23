import random

n = int(input())  # количество попыток

for i in range(n):
    a = random.randrange(1, 2)
    if a == 1:
        print('Орел')
    if a == 2:
        print('Решка')
