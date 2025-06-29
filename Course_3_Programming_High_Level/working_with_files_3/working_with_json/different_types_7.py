import json


def different_types():
    with open('data.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

    updated_data = []

    for row in data:
        if isinstance(row, str):
            updated_data.append(row + '!')
        elif type(row) == bool:
            updated_data.append(not row)
        elif isinstance(row, int):
            updated_data.append(row + 1)
        elif isinstance(row, list):
            updated_data.append(row + row)
        elif isinstance(row, dict):
            row.update({"newkey": None})
            updated_data.append(row)
        elif row is None:
            pass

    with open('updated_data.json', 'w', encoding='UTF-8') as updated:
        json.dump(updated_data, updated, ensure_ascii=False, indent=3)


different_types()
