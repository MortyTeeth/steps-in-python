col = int(input())

for i in range(1, col + 1):
    string = input()
    if string.isspace() == True or string == '':
        print(i, ':', ' COMMENT SHOULD BE DELETED', sep = '')
    else:
        print(i, ':', ' ', string, sep = '')