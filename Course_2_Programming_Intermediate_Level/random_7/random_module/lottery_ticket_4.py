import random

i = 0
line = []
while i < 7:
    a = random.randrange(1, 50)
    if a not in line:
        line.append(a)
        i += 1
print(*sorted(line))
