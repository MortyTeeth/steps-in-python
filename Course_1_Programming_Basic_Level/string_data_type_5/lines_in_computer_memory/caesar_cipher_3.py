a = int(input())
string = input()
finaltxt = ''

for i in range(len(string)):
    n = ord(string[i]) - a
    if n < 97:
        n = 122 - (96 - n)
    print(chr(n), end = '')