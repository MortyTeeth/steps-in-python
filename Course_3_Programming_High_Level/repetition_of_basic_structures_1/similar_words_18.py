def similar_words(w_f_c):
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    for char in w_f_c:
        if char in vowels:
            w_f_c = w_f_c.replace(char, '0')
        else:
            w_f_c = w_f_c.replace(char, '1')

    len_w_f_c = len(w_f_c)

    list_with_words = []

    count_numbers = int(input())

    for i in range(count_numbers):
        word = input()
        list_with_words.append(word)

    list_with_words_after_edit = []

    for word in list_with_words:
        for symbol in word:
            if symbol in vowels:
                word = word.replace(symbol, '0')
            else:
                word = word.replace(symbol, '1')
        list_with_words_after_edit.append(word)

    dictionary = dict(zip(list_with_words, list_with_words_after_edit))

    for key, value in dictionary.items():
        if w_f_c.count('0') == value[:len_w_f_c].count('0') and (
                w_f_c == value[:len_w_f_c] or w_f_c[:len(value)] == value):
            print(key)


word_for_check = input()

similar_words(word_for_check)
