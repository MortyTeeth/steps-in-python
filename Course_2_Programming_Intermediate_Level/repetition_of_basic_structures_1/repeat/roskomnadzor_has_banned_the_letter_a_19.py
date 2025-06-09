def has_banned_the_letter_a(w):
    simple_str = ' запретил букву'
    lower_symbols = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                     'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    word = w + simple_str
    for symbol in lower_symbols:
        if symbol in word:
            print(word, symbol)
            word = word.replace(symbol, '').replace('  ', ' ').strip()


word = input()

has_banned_the_letter_a(word)
