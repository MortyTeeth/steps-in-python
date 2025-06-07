col = int(input())

l = []

count = 0

for i in range(col):
    word = input()
    if word not in l:
        l.append(word)
print(*l, sep='\n')