from itertools import groupby


def word_groups(line):
    words = line.split()
    sorted_len = sorted(words, key=lambda x: (len(x), 0))
    group = groupby(sorted_len, key=lambda x: len(x))
    for key, value in group:
        print(f'{key} -> {", ".join(i for i in sorted(value))}')


string = input()
word_groups(string)
