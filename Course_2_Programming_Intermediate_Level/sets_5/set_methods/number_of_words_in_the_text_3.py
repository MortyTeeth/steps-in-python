def number_of_words_in_the_text(text):
    punctuation_marks = '.,;:-?!'
    text_after_corrections = ''
    for i in range(len(text)):
        if text[i] not in punctuation_marks:
            text_after_corrections += text[i]

    text_after_lower = text_after_corrections.lower()
    list_after_all = text_after_lower.split()
    final_set = set(list_after_all)
    print(len(final_set))


text = input()

number_of_words_in_the_text(text)