from collections import Counter


def word_search(list_words):
    lower_list_words = [i.lower() for i in list_words]
    counter = Counter(lower_list_words)
    min_repeat = min(counter.most_common(), key=lambda x: x[1])[1]
    list_with_words_with_min_repeats = [i for i in counter.items() if i[1] == min_repeat]
    sorted_list = dict(sorted(list_with_words_with_min_repeats, key=lambda x: x[0]))
    print(', '.join(sorted_list.keys()))


words = input().split()

word_search(words)
