def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_suits = ["пик", "треф", "бубен", "червей"]
    card_suits.remove(suit)

    while True:
        for suit in card_suits:
            for value in card_values:
                yield value + ' ' + suit
