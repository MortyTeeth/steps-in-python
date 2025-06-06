s = input()

if len(s) % 2 == 0:
    first = s[:len(s) // 2]
    second = s[len(s) // 2 :]
    print(second, first,sep = '')
else:
    first = s[:len(s) // 2 + 1]
    second = s[len(s) // 2 + 1 :]
    print(second, first,sep = '')