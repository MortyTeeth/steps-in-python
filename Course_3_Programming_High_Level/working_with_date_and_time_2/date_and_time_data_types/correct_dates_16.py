from datetime import date

count = 0

d = input()
list_with_status = []

while d != 'end':
    try:
        d = d.split('.')
        d = [int(i) for i in d]
        d = date(d[2], d[1], d[0])
        list_with_status.append('Корректная')
        count += 1
    except:
        list_with_status.append('Некорректная')
    d = input()
print(*list_with_status, sep='\n')
print(count)
