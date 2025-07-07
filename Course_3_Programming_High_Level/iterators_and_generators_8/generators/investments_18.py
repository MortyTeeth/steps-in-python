def investments():
    with open('data.csv', 'r', encoding='UTF-8') as csv_file:
        data = (line for line in csv_file)
        line_values = (line.rstrip().split(',') for line in data if line)
        file_headers = next(line_values)
        line_dicts = (dict(zip(file_headers, data)) for data in line_values)

        invest = list((i['raisedAmt'] for i in line_dicts if i['round'] == 'a'))
        print(sum([int(i) for i in invest]))


investments()
