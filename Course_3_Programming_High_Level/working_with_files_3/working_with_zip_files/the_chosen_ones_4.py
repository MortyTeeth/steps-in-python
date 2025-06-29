from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip', 'r') as zipfile:
    data = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
    dictionary = {}
    info = zipfile.infolist()

    for file in info:
        file_datatime = datetime(*file.date_time)
        if file_datatime > data:
            dictionary.update({file.filename: file.date_time})

    new_dictionary = {}

    for key, value in dictionary.items():
        if key[-1] == '/':
            pass
        else:
            new_dictionary.update({key: value})

    last_dict = {}

    for key, value in new_dictionary.items():
        if '/' in key:
            last_dict.update({key.split('/')[1]: value})
        else:
            last_dict.update({key: value})

    sorted_dict = dict(sorted(last_dict.items(), key=lambda x: x[0]))

    for key, value in sorted_dict.items():
        print(key)
