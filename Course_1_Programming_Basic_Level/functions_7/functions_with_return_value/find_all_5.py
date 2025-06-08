def find_all(target, symbol):
    l = []
    for i in range(len(target)):
        position = 0
        if symbol == target[i]:
            l.append(i)
    return l
    pass


s = input()
char = input()

print(find_all(s, char))