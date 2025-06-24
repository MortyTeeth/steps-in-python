def dictionary_of_synonyms(n):
    dictionary_for_all = {}

    for i in range(n):
        line = input().split()
        dictionary_for_all.update({line[0]: line[1]})

    value_word = input()

    for key, value in dictionary_for_all.items():
        if value_word == value:
            print(key)

    for key, value in dictionary_for_all.items():
        if value_word == key:
            print(value)


num_of_pairs = int(input())

dictionary_of_synonyms(num_of_pairs)
