from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zipfile:
    info = zipfile.infolist()
    dictionary_with_file = {}

    for file in info:
        if '/' in file.filename and len(file.filename.split('/')[1]) > 1:
            second_part_name = file.filename.split('/')[1]
            dictionary_with_file.update({second_part_name: [f'  Дата модификации файла: {datetime(*file.date_time)}',
                                                            f'  Объем исходного файла: {file.file_size} байт(а)',
                                                            f'  Объем сжатого файла: {file.compress_size} байт(а)']})
        elif '/' in file.filename and len(file.filename.split('/')[1]) == 0:
            pass
        else:
            dictionary_with_file.update({file.filename: [f'  Дата модификации файла: {datetime(*file.date_time)}',
                                                         f'  Объем исходного файла: {file.file_size} байт(а)',
                                                         f'  Объем сжатого файла: {file.compress_size} байт(а)']})

    sorted_dictionary = dict(sorted(dictionary_with_file.items(), key=lambda x: x[0]))

    for key, value in sorted_dictionary.items():
        print(key)
        print(value[0])
        print(value[1])
        print(value[2])
        print()
