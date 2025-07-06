class CardDeck:
    def __init__(self):
        self.cards = []
        suits = ('пик', 'треф', 'бубен', 'червей')
        meanings = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        for suit in suits:
            for meaning in meanings:
                self.cards.append((meaning + ' ' + suit))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        else:
            card = self.cards[self.index]
            self.index += 1
            return card
