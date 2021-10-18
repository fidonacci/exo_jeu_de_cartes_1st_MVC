"""Define the Deck."""

import random
from collections import UserList

from models.card import RANKS, SUITS, Card


class Deck(UserList):
    """Deck of cards."""

    def __init__(self):
        """Has some cards."""
        self.data = []
        # import pdb; pdb.set_trace()
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.data.append(card)

        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self)

    def draw_card(self):
        """Draw the top card."""
        try:
            return self.pop()
        except IndexError:
            return None


if __name__ == "__main__":
    d = Deck()
    print(d)
