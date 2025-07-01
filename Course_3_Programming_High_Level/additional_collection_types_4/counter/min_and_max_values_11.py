from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')


def min_values():
    min_length = min(data.items(), key=lambda x: x[1])[1]
    list_with_min = [i for i in data.items() if i[1] == min_length]
    return list_with_min


def max_values():
    max_length = max(data.items(), key=lambda x: x[1])[1]
    list_with_max = [i for i in data.items() if i[1] == max_length]
    return list_with_max


data.min_values = lambda: min_values()
data.max_values = lambda: max_values()
