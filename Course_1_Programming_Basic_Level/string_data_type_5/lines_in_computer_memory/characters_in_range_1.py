a = int(input())
b = int(input())

for i in range(0, b - a + 1):
    print(chr(ord(chr(a)) + i), sep = ' ', end = ' ')