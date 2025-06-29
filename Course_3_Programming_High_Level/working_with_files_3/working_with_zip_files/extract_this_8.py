from zipfile import ZipFile


def extract_this(zip_name, *args):
    args = [*args]
    with ZipFile(zip_name, 'r') as zipfile:
        if len(args) == 0:
            zipfile.extractall()
        else:
            for file in args:
                zipfile.extract(file)
