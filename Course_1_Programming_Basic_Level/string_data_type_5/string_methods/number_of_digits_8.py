string = input()

count = 0

strings = '0123456789'

for i in range(len(string)):
    if string[i] in strings:
        count += 1
print(count)  