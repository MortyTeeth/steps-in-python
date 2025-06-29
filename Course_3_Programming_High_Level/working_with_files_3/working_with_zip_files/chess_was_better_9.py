from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        json.loads(string)  # Проверяем, можно ли распарсить JSON
        return True
    except json.JSONDecodeError:
        return False


with ZipFile('data.zip', 'r') as zipfile:
    json_list = []
    for file in zipfile.namelist():  # Получаем список файлов
        with zipfile.open(file) as f:  # Открываем файл в архиве
            try:
                data = f.read().decode('utf-8')  # Декодируем в строку
                if is_correct_json(data):  # Проверяем корректность JSON
                    json_list.append(data)
            except UnicodeDecodeError:  # Если не удаётся декодировать в UTF-8
                pass

    full_name_dict = {}

    for f_player in json_list:
        f = json.loads(f_player)
        if f['team'] == 'Arsenal':
            full_name_dict.update({f['first_name']: f['last_name']})

    sorted_dict = dict(sorted(full_name_dict.items(), key=lambda x: (x[0], x[1])))

    for key, value in sorted_dict.items():
        print(key, value)
