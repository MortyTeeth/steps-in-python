num = int(input())

kod = '11'
count = 0

for i in range(num):
    string = input()
    if string.count(kod) >= 3:
        count += 1
print(count)