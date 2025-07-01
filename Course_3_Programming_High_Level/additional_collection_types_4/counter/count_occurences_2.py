from collections import Counter


def count_occurences(word, words):
    word_lower = word.lower()
    lower_words = words.lower()
    split_words = lower_words.split(' ')
    num = Counter(split_words)
    return num[word_lower]
