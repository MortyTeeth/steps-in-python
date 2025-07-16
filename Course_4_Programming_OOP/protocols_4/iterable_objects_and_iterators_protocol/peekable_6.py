_sentinel = object()


class Peekable:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._buffer = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._buffer:
            return self._buffer.pop(0)
        return next(self._iterator)

    def peek(self, default=_sentinel):
        if self._buffer:
            return self._buffer[0]
        try:
            value = next(self._iterator)
            self._buffer.append(value)
            return value
        except StopIteration:
            if default is _sentinel:
                raise
            return default
