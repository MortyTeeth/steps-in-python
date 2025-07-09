def intersperse(iterable, delimiter):
    iterator = iter(iterable)
    try:
        yield next(iterator)
        for item in iterator:
            yield delimiter
            yield item
    except StopIteration:
        pass
