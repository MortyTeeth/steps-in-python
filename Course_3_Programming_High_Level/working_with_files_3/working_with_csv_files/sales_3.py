with open('sales.csv', 'r', encoding='UTF-8') as file:
    data = file.read()
    rows = [r.split(';') for r in data.splitlines()]
    del rows[0]
    for row in rows:
        if int(row[2]) < int(row[1]):
            print(row[0])
