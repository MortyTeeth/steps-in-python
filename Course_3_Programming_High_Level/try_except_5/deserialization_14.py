import json


def deserialization(json_name):
    try:
        with open(json_name, 'r', encoding='UTF-8') as json_file:
            try:
                data = json.load(json_file)
                print(data)
            except:
                print('Ошибка при десериализации')
    except:
        print('Файл не найден')


json_name = input()
deserialization(json_name)
