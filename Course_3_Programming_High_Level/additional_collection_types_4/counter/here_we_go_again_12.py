from collections import Counter

with open('name_log.csv', 'r', encoding='UTF-8') as csv_file:
    data = csv_file.read()
    rows = [i.split(',') for i in data.splitlines()]
    del rows[0]
    rows_mail = [i[1] for i in rows]
    counter = Counter(rows_mail)
    sorted_counter = Counter(sorted(counter.items(), key=lambda x: x[0]))

    for key, value in sorted_counter:
        print(f'{key}: {value}')
