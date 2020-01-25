from Deck import Deck
from PlaySpace import PlaySpace
from Players import User, AllUsers

public_deck = Deck()
public_play_space = PlaySpace()
players: AllUsers
players_count = -1
hand_counts = []


def populate_hands():
    global players
    players_list = []
    for player in range(players_count):
        hand = []
        for i in range(7):
            card = public_deck.get_random_card()
            hand.append(card)
        players_list.append(User(hand=hand, name=get_player_details(player)))
    players = AllUsers(player_list=players_list)


def get_players_count():
    while True:
        try:
            return int(input("Enter total players"))
        except ValueError:
            print("Invalid input, try again")


def get_player_details(count: int):
    return input("Enter player name" + str(count))


def get_card_input(whose_turn):
    while True:
        try:
            val = int(input("Play a card")) - 1
            if val < 0 or val >= len(whose_turn.hand):
                raise ValueError
            return val
        except ValueError:
            print("Invalid input, try again")


def populate_hand_counts():
    global hand_counts
    hand_counts_tmp = []
    for item in players.players:
        hand_counts_tmp.append(len(item.hand))
    hand_counts = hand_counts_tmp


def display_cards(player: User):
    print("Hand of", player.name)
    for i, card in enumerate(player.hand):
        print(str(i+1), ") ", card.color, card.name)


def run_game():
    while 0 not in hand_counts:
        whose_turn = players.current_player

        no_cards_playable = True
        for card in whose_turn.hand:
            if public_play_space.can_play(card):
                no_cards_playable = False

        if no_cards_playable:

            """ Draw a card """
            drawn_card_valid = False
            while not drawn_card_valid:
                drawn_card = public_deck.draw_top_card()
                print("Drew card:", drawn_card.color, drawn_card.name)
                if public_play_space.can_play(drawn_card):

                    """ add drawn card to inventory """
                    whose_turn.add_card(drawn_card)
                    drawn_card_valid = True
                else:
                    print("Cant play the drawn card:", drawn_card.color, drawn_card.name)
                    """ Add drawn card to players inventory """
                    whose_turn.add_card(drawn_card)

        """ Enter a loop to force user to play a valid card """
        valid = False
        while not valid:
            display_cards(whose_turn)
            """ Gets index of card from users inventory """
            card_number = get_card_input(whose_turn=whose_turn)

            """ Get the card from inventory of user """
            card = whose_turn.get_card(card_number)

            """ Checks if card played is valid """
            if public_play_space.can_play(card):

                """ Plays card from Users inventory """
                whose_turn.remove_card(card)

                """ Adds card played to play space """
                public_play_space.add_card(card)

                whose_turn = players.next_player(card)

                valid = True
            else:
                print("That card cant be played")
                valid = False

        """ Updates hand count of each player"""
        populate_hand_counts()
    print(players.players[hand_counts.index(0)].name, "Wins!")


if __name__ == '__main__':
    players_count = get_players_count()
    populate_hands()
    populate_hand_counts()
    run_game()
