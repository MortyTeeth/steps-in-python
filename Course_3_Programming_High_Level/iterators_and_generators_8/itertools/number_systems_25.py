from itertools import product


def number_systems(n, l):
    yo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for m in product(yo[:n], repeat=l):
        print(''.join(m), sep='', end=' ')


notation = int(input())
len_str = int(input())

number_systems(notation, len_str)
