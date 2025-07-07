def parse_ranges(ranges):
    ranges_split = ranges.split(',')
    numbers = [i.split('-') for i in ranges_split]
    for i in numbers:
        yield from list(range(int(i[0]), int(i[1]) + 1))
