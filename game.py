import random

from Cards import NumberCards
from Cards import SpecialCards
from Deck import Deck
from PlaySpace import PlaySpace
from Players import User

public_deck = Deck()
public_play_space = PlaySpace()
whose_turn: User
players = []
players_count = -1
hand_counts = []


def populate_hands():
    for player in range(players_count):
        hand = []
        for i in range(7):
            card = public_deck.get_random_card()
            hand.append(card)
        players.append(User(hand=hand, name=get_player_details(player)))


def get_players_count():
    return int(input("Enter total players"))


def get_player_details(count: int):
    return input("Enter player name" + str(count))


def first_player():
    """ Decides first player """
    global whose_turn
    whose_turn = random.choice(players)


def populate_hand_counts():
    global hand_counts
    hand_counts_tmp = []
    for item in players:
        hand_counts_tmp.append(len(item.hand))
    hand_counts = hand_counts_tmp


def display_cards(player: User):
    print("Hand of", player.name)
    for i, card in enumerate(player.hand):
        print(str(i+1), ") ", card.color, card.name)


def run_game():
    global whose_turn
    while 0 not in hand_counts:
        current_player_index = players.index(whose_turn)

        no_cards_playable = True
        for card in whose_turn.hand:
            if public_play_space.can_play(card):
                no_cards_playable = False

        if no_cards_playable:

            """ Draw a card """
            drawn_card_valid = False
            while not drawn_card_valid:
                drawn_card = public_deck.draw_top_card()
                if public_play_space.can_play(drawn_card):

                    """ add drawn card to inventory """
                    print("Drew card:", drawn_card.color, drawn_card.name)
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
            card_number = int(input("Play a card")) - 1

            """ Get the card from inventory of user """
            card = whose_turn.get_card(card_number)

            """ Checks if card played is valid """
            if public_play_space.can_play(card):

                """ Plays card from Users inventory """
                whose_turn.remove_card(card)

                """ Adds card played to play space """
                public_play_space.add_card(card)

                valid = True
            else:
                print("That card cant be played")
                valid = False

        """ Rotates player turns """
        if current_player_index + 1 > (len(players) - 1):
            whose_turn = players[0]
        else:
            whose_turn = players[current_player_index + 1]

        """ Updates hand count of each player"""
        populate_hand_counts()
    print(players[hand_counts.index(0)].name, "Wins!")


if __name__ == '__main__':
    players_count = get_players_count()
    populate_hands()
    populate_hand_counts()
    first_player()
    run_game()
