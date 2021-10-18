class View:
    def prompt_for_players(self):
        name = input("Write player name :")
        if not name:
            return None
        return name

    def show_player_hand(self, name, hand):
        print(f"[Player {name}]")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("Hidden card")

    def prompt_for_filp_cards(self):
        print()
        input("Ready to flip the cards ?")
        return True

    def show_winner(self, name):
        print(f"Congrats {name}")

    def prompt_for_new_game(self):
        print("Do you want to replay ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True
