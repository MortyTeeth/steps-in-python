num = int(input())
s = []
for i in range(97, num + 97, 1):
    s += chr(i)
print(s)