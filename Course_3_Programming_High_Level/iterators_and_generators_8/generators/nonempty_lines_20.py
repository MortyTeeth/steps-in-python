def nonempty_lines(file):
    with open(file, 'r', encoding='UTF-8') as file:
        for line in file:
            if len(line) > 25:
                yield '...'
            else:
                line = line.rstrip('\n')
                if line != '':
                    yield line
