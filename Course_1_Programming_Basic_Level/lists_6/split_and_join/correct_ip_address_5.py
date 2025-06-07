ip = input()

otd = ip.split('.')

count = 0

for i in range(len(otd)):
    if  0 <= int(otd[i]) <= 255:
        count += 1
if count == 4:
    print('ДА')
else:
    print('НЕТ')