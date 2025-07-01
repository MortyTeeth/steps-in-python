from collections import Counter


def words_of_a_certain_length(list_with_words):
    len_in_words = [len(i) for i in list_with_words]
    counter_len = Counter(len_in_words).most_common()
    counter_len = sorted(counter_len, key=lambda tup: (tup[1], counter_len))

    for key, value in counter_len:
        print(f'Слов длины {key}: {value}')


words = input().split()

words_of_a_certain_length(words)
