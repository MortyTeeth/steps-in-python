from collections import Counter


def scrabble(symbols, word):
    symbols_lower = symbols.lower()
    word_lower = word.lower()
    first_counter = Counter(symbols_lower)
    second_counter = Counter(word_lower)
    if first_counter >= second_counter:
        return True
    else:
        return False
