def wifi_moscow():
    with open('wifi.csv', 'r', encoding='UTF-8') as file:
        data = file.read()
        rows = [r.split(';') for r in data.splitlines()]
        del rows[0]
        new_list = []
        for row in rows:
            new_list.append([row[1], row[3]])
        dict_with_all_points = dict()

        for row in new_list:
            if row[0] not in dict_with_all_points:
                dict_with_all_points.update({row[0]: int(row[1])})
            else:
                dict_with_all_points.update({row[0]: dict_with_all_points[row[0]] + int(row[1])})

        sorted_dict = dict(sorted(dict_with_all_points.items(), key=lambda x: (-x[1], x[0])))

        for key, value in sorted_dict.items():
            print(f'{key}: {value}')


wifi_moscow()
