def programmers_dictionary(n_w_i_d):
    exp = ':'
    first_dict = {}
    second_dict = {}
    for i in range(n_w_i_d):
        list_1 = input()
        list_after_edit = ''
        for k in range(len(list_1)):
            if list_1[k] not in exp:
                list_after_edit += list_1[k]
        list_2 = list_after_edit.split()
        dict_for_add = {list_2[0].lower(): list_2[1:]}
        first_dict.update(dict_for_add)

    number_of_search_words = int(input())

    list_for_key_words = []

    for k in range(number_of_search_words):
        list_2 = input()
        list_for_key_words.append(list_2.lower())

    for key in list_for_key_words:
        if key in first_dict:
            print(*first_dict[key])
        else:
            print('Не найдено')


num_words_in_dict = int(input())

programmers_dictionary(num_words_in_dict)
