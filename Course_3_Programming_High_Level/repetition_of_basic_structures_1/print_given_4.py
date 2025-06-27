def print_given(*args, **kwargs):
    dictionary = dict()
    for i in args:
        print(i, type(i))
    for key, value in kwargs.items():
        dictionary.update({key: [value, type(value)]})
    dictionary = sorted(dictionary.items(), key=lambda x: x[0])
    for key, value in dictionary:
        print(key, *value)
