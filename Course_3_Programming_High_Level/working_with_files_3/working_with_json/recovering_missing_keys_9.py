import json


def recovering_missing_keys():
    with open('people.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        all_keys = []

        for dictionary in data:
            for key, value in dictionary.items():
                if key not in all_keys:
                    all_keys.append(key)

    with open('updated_people.json', 'w', encoding='UTF-8') as updating:
        for dictionary in data:
            for must_key in all_keys:
                if must_key in dictionary:
                    pass
                else:
                    dictionary.update({must_key: None})
        updating.write(json.dumps(data, indent=3))


recovering_missing_keys()
