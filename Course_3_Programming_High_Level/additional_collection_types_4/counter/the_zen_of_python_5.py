from collections import Counter
from string import ascii_lowercase

with open('pythonzen.txt', 'r', encoding='UTF-8') as text:
    data = text.read()
    data_lower = data.lower()
    data_without_spaces = ''.join([i for i in data_lower])
    data_without_shit_symbols = ''.join([i for i in data_without_spaces if i in ascii_lowercase])

    data_counter = Counter(data_without_shit_symbols)
    sorted_data = dict(sorted(data_counter.items(), key=lambda x: x[0]))
    for symbol, num in sorted_data.items():
        print(f'{symbol}: {num}')
