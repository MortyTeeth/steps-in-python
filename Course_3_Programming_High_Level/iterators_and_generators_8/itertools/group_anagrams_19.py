from itertools import groupby


def group_anagrams(words):
    sorted_words = sorted(words, key=lambda x: ''.join(sorted(x)))
    grouped = groupby(sorted_words, key=lambda x: ''.join(sorted(x)))

    result = [tuple(group) for _, group in grouped]
    return result