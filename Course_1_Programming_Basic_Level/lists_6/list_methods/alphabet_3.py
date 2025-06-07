count = 0

l = []

for i in range(26):
    count += 1
    l.append(chr(97 + i) * count)
print(l)