from zipfile import ZipFile

with ZipFile('workbook.zip') as zipfile:
    info = zipfile.infolist()
    count = 0

    for file in info:
        if file.is_dir() == False:
            count += 1
    print(count)
