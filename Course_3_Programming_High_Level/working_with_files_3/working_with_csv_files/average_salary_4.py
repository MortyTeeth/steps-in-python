with open('salary_data.csv', 'r', encoding='UTF-8') as file:
    data = file.read()
    rows = [r.split(';') for r in data.splitlines()]
    del rows[0]

    for l in rows:
        l.append('1')

    dict_with_all = dict()

    for row in rows:
        if row[0] not in dict_with_all:
            dict_with_all.update({row[0]: (int(row[1]), int(row[2]))})
        else:
            dict_with_all.update({row[0]: (dict_with_all[row[0]][0] + int(row[1]), dict_with_all[row[0]][1] + 1)})

    dict_with_middle_meaning = dict()

    for key, value in dict_with_all.items():
        dict_with_middle_meaning.update({key: value[0] / value[1]})

    sorted_dict = dict(sorted(dict_with_middle_meaning.items(), key=lambda x: (x[1], x[0])))

    for key, value in sorted_dict.items():
        print(key)
