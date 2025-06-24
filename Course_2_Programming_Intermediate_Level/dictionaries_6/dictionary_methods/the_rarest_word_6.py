def rarest_word(txt):
    compile_to_lower = txt.lower()
    exception = '.,!?:;-'

    compile_to_need = ''
    for i in range(len(compile_to_lower)):
        if compile_to_lower[i] not in exception:
            compile_to_need += compile_to_lower[i]

    spisok_slov = compile_to_need.split()

    words_and_their_numbers = {}

    for word in spisok_slov:
        if word not in words_and_their_numbers:
            words_and_their_numbers[word] = 1
        else:
            words_and_their_numbers[word] += 1

    min_ch = min(words_and_their_numbers.values())

    dict_with_small = {}

    for key, value in words_and_their_numbers.items():
        if value == min_ch:
            dict_with_small.update({key: value})

    print(min(dict_with_small))


text = input()

rarest_word(text)
