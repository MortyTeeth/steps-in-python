import pickle
import sys

file_name, *data = list(map(str.strip, sys.stdin))


def alone_function(file_name, data):
    with open(file_name, mode='rb') as file:
        alone_function = pickle.load(file)
        return alone_function(*data)


print(alone_function(file_name, data))
