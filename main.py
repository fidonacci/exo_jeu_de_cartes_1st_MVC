from controller import Controller
from view import View
from models.deck import Deck


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)

    game.run()


if __name__ == "__main__":
    main()

