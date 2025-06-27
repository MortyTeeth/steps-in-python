def difficulties_in_translation(c_p):
    dictionary = dict()
    for i in range(c_p):
        line = input().split(', ')
        for language in line:
            if language not in dictionary:
                dictionary.update({language: 1})
            else:
                dictionary.update({language: dictionary[language] + 1})
    good_language = {}
    for key, value in dictionary.items():
        if value == c_p:
            good_language.update({key: value})
    if len(good_language) == 0:
        print('Сериал снять не удастся')
    else:
        print(*sorted(good_language.keys()), sep=', ')


count_people = int(input())

difficulties_in_translation(count_people)
