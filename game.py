import random

from Cards import NumberCards
from Cards import SpecialCards
from Players import User


colors = ["red", "blue", "green", "yellow"]
public_deck = []
public_play_space = []
whose_turn: User
players = []
players_count = -1
hand_counts = []


def populate_deck():
    """ Populate the deck """

    for i in range(80):
        card_types = [NumberCards.NumberCards(color=random.choice(colors), number=random.randint(0, 9)),
                      SpecialCards.Reverse(color=random.choice(colors)), SpecialCards.Skip(color=random.choice(colors))]
        public_deck.append(random.choice(card_types))


def populate_hands():
    for player in range(players_count):
        hand = []
        for i in range(7):
            card = random.choice(public_deck)
            hand.append(card)
            public_deck.remove(card)
        players.append(User(hand=hand, name=get_player_details(player)))


def get_players_count():
    return int(input("Enter total players"))


def get_player_details(count: int):
    return input("Enter player name" + str(count))


def first_player():
    global whose_turn
    whose_turn = random.choice(players)


def populate_hand_counts():
    for item in players:
        hand_counts.append(len(item.hand))


def display_cards(player: User):
    print("Hand of", player.name)
    for i, card in enumerate(player.hand):
        if card.type == "SPECIAL":
            print(str(i+1), ") ", card.color, card.name)
        else:
            print(str(i+1), ") ", card.color, card.number)


def run_game():
    global whose_turn
    while 0 not in hand_counts:
        current_player_index = players.index(whose_turn)
        display_cards(whose_turn)
        card_number = int(input("Play a card")) - 1
        card = whose_turn.play_card(card_number)
        public_play_space.append(card)
        if current_player_index + 1 > (len(players) - 1):
            whose_turn = players[0]
        else:
            whose_turn = players[current_player_index + 1]


if __name__ == '__main__':
    players_count = get_players_count()
    populate_deck()
    populate_hands()
    populate_hand_counts()
    first_player()
    run_game()
