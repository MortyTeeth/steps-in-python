x = input()
file = open(x, 'r+', encoding='utf-8')
result = [line.rstrip() for line in file.readlines()]
print(result[-2])
file.close()
