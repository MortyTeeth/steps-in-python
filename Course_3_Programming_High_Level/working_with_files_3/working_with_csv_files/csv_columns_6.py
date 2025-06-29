def csv_columns(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = file.read()
        rows = [r.split(',') for r in data.splitlines()]
        keys = rows[0]
        values = rows[1:]
        result = {key: [] for key in keys}

        for row in values:
            for key, value in zip(keys, row):
                result[key].append(value)

        return result
