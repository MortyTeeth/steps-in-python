from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode="r"):
    try:
        with open(filename, mode) as f:
            yield (f, None)
            f.close()
    except Exception as err:
        yield (None, err)
