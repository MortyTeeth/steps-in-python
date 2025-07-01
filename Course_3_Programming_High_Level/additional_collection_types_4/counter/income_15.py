from collections import Counter
import json
import time


def income():
    counter = Counter()
    for i in range(1, 5):
        with open(f'quarter{i}.csv', 'r', encoding='UTF-8') as csv_file:
            data = csv_file.read()
            rows = [row.split(',') for row in data.splitlines()]
            del rows[0]
            rows_add = Counter({row[0]: int(row[1]) + int(row[2]) + int(row[3]) for row in rows})
            counter += rows_add

    with open('prices.json', 'r', encoding='UTF-8') as json_file:
        data2 = json.load(json_file)
        total_income = 0

        for key, value in counter.items():
            for key2, value2 in data2.items():
                if key == key2:
                    total_income += value * value2
    print(total_income)


income()
