from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as pickle_file:
    obj = pickle.load(pickle_file)

    for animal in obj:
        for field, value in zip(Animal._fields, animal):
            print(field + ':', value)
        print()
