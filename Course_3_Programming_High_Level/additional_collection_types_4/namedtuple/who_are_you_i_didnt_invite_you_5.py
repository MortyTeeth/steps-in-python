from datetime import datetime

with open('meetings.csv', 'r', encoding='UTF-8') as csv_file:
    data = csv_file.read()
    rows = [r.split(',') for r in data.splitlines()]
    del rows[0]
    sorted_list = sorted(rows, key=lambda x: datetime.strptime((x[2] + ' ' + x[3]), '%d.%m.%Y %H:%M'))
    for user in sorted_list:
        print(user[0] + ' ' + user[1])
