from collections import Counter


def print_bar_chart(data, mark):
    if isinstance(data, str):
        counter = Counter(data).most_common()
        for key, value in counter:
            print(f'{key} |{value * mark}')
    else:
        counter = Counter(data).most_common()
        max_len_key = len(max(Counter(data).items(), key=lambda x: int(len(x[0])))[0])
        for key, value in counter:
            print(f'{key.ljust(max_len_key, " ")} |{value * mark}')
