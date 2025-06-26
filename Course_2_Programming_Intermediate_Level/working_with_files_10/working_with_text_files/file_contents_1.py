x = input()
file = open(x, 'r', encoding='utf-8')

for line in file:
    print(line.strip())

file.close()
