line = input().split()
matrix = [[line[0]]]

for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        matrix[-1].append(line[i])
    else:
        matrix.append([line[i]])
print(matrix)