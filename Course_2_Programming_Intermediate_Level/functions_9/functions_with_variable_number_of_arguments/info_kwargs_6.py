def info_kwargs(**kwargs):
    sorted_dict = dict(sorted(kwargs.items()))

    for key, value in sorted_dict.items():
        print(str(key) + ': ' + str(value))
