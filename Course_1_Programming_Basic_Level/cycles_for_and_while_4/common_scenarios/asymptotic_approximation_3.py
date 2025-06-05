import math

n = int(input())
sum = 0
for i in range(1, n + 1):
    c = 1 / i
    sum = sum + c

itog = sum - math.log(n)
print(itog)