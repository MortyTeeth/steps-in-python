from contextlib import contextmanager


@contextmanager
def safe_write(filename):
    file = open(filename, 'a', encoding='u8')
    cursor = file.tell()
    try:
        yield file
    except Exception as err:
        file.truncate(cursor)
        print('Во время записи в файл было возбуждено исключение', type(err).__name__)
    finally:
        file.close()
