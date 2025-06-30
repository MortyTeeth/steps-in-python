from collections import defaultdict


def best_sender(mes, sen):
    result = defaultdict(int)

    for message, sender in zip(mes, sen):
        len_mes_split = len(message.split())
        result[sender] += len_mes_split

    max_word = max(result.items(), key=lambda x: x[1])[1]
    filter_with_max = dict(filter(lambda x: x[1] == max_word, result.items()))

    sorted_len_in_name = sorted(filter_with_max.keys(), key=lambda x: -len(list(x)))
    return sorted_len_in_name[0]
