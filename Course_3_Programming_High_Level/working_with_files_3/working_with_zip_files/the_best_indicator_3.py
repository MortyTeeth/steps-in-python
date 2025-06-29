from zipfile import ZipFile

with ZipFile('workbook.zip') as zipfile:
    info = zipfile.infolist()
    dict_with_all_info = {}

    for file in info:
        if file.compress_size == 0 or file.file_size == 0:
            pass
        else:
            dict_with_all_info.update({file.filename: (file.compress_size / file.file_size) * 100})
    min_name_file = min(dict_with_all_info, key=lambda x: dict_with_all_info[x])

    print(min_name_file.split('/')[-1])
