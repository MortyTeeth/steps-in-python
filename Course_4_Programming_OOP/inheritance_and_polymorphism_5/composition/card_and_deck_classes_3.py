import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"


class Deck:
    def __init__(self):
        self.suits = ["♣", "♢", "♡", "♠"]
        self.ranks = "2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A".split(", ")
        self.suits_and_ranks = []
        for suit in self.suits:
            for rank in self.ranks:
                self.suits_and_ranks.append(f"{suit}{rank}")

    def __str__(self):
        return f"Карт в колоде: {len(self.suits_and_ranks)}"

    def shuffle(self):
        if len(self.suits_and_ranks) == 52:
            random.shuffle(self.suits_and_ranks)
        else:
            raise ValueError("Перемешивать можно только полную колоду")

    def deal(self):
        if len(self.suits_and_ranks) > 0:
            last_card = self.suits_and_ranks[-1]
            del self.suits_and_ranks[-1]
            return Card(last_card[0], last_card[1:])
        else:
            raise ValueError("Все карты разыграны")
