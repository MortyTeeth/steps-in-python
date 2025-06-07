s = input().split()

l = []

for i in range(len(s)):
    l.append(int(s[i]))

l.sort()
print(*l)
l.sort(reverse=True)
print(*l)