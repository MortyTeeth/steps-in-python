from string import *

with (open('file.txt', 'r', encoding='utf-8')) as file:
    number_of_letters_of_the_latin_alphabet = 0
    words = 0
    lines = 0
    for line in file:
        lines += 1
        vr_result_word = len([i for i in line.split()])
        words += vr_result_word
        for symbols in line:
            if symbols in (ascii_lowercase + ascii_uppercase):
                number_of_letters_of_the_latin_alphabet += 1

    print('Input file contains:')
    print(str(number_of_letters_of_the_latin_alphabet) + ' letters')
    print(str(words) + ' words')
    print(str(lines) + ' lines')
