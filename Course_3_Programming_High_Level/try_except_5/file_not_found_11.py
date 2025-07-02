def file_not_found(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as file:
            data = file.read()
            print(data)
    except:
        print('Файл не найден')


file_name = input()
file_not_found(file_name)
