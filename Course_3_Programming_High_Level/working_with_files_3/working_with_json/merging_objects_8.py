import json


def merging_objects():
    with open('data1.json', 'r', encoding='UTF-8') as file_1, open('data2.json', 'r', encoding='UTF-8') as file_2:
        data_1 = json.load(file_1)
        data_2 = json.load(file_2)

        dict_for_all = dict()

        for key, value in data_1.items():
            dict_for_all.update({key: value})

        for key, value in data_2.items():
            dict_for_all.update({key: value})

    with open('data_merge.json', 'w', encoding='UTF-8') as data_merge:
        data_merge.write(json.dumps(dict_for_all, indent=3, sort_keys=True))


merging_objects()
