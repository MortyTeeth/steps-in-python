from random import *

k = 0
n = 10 ** 6
r = 1
S = 4

for i in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        k += 1
print((k / n) * S)
