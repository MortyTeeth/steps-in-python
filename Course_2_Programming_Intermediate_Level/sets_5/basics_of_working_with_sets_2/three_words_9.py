def three_words(main_list):
    first_word = set(main_list[0])
    second_word = set(main_list[1])
    third_word = set(main_list[2])
    if first_word == second_word == third_word:
        print('YES')
    else:
        print('NO')


main_list = input().split()

three_words(main_list)
