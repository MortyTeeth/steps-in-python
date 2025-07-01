from collections import Counter


def word_search(list_words):
    lower_list_words = [i.lower() for i in list_words]
    counter = Counter(lower_list_words)
    max_repeat = max(counter.most_common(), key=lambda x: x[1])[1]
    list_with_words_with_max_repeats = [i for i in counter.items() if i[1] == max_repeat]
    print(max(list_with_words_with_max_repeats, key=lambda x: x[0])[0])


words = input().split()

word_search(words)
