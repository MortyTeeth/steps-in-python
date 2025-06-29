from zipfile import ZipFile

with ZipFile('workbook.zip', 'r') as zipfile:
    info = zipfile.infolist()

    file_size_behind = 0
    file_size_after = 0

    for file in info:
        file_size_behind += file.file_size
        file_size_after += file.compress_size
    print(f'Объем исходных файлов: {file_size_behind} байт(а)')
    print(f'Объем сжатых файлов: {file_size_after} байт(а)')
