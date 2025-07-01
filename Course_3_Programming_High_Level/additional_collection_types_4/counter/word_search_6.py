from collections import Counter


def word_search(list_words):
    lower_list_words = [i.lower() for i in list_words]
    counter = Counter(lower_list_words)
    print(counter.most_common()[0][0])


words = input().split()

word_search(words)
