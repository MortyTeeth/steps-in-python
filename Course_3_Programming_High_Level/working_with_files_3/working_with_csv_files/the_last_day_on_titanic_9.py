def the_last_day_on_titanic():
    with open('titanic.csv', 'r', encoding='UTF-8') as file:
        data = file.read()
        rows = [r.split(';') for r in data.splitlines()]
        del rows[0]
        new_rows = []
        for row in rows:
            if int(row[0]) == 1 and float(row[3]) < 18:
                new_rows.append(row)
        sorted_rows = sorted(new_rows, key=lambda x: x[2], reverse=True)
        for row in sorted_rows:
            print(row[1])


the_last_day_on_titanic()