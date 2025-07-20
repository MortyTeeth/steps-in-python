from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    original_stdout = sys.stdout.write
    sys.stdout.write = lambda text: original_stdout(text[::-1])
    try:
        yield
    finally:
        sys.stdout.write = original_stdout
