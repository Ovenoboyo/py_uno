class User(object):
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def add_card(self, card):
        self.hand.append(card)

    def get_card(self, number: int):
        return self.hand[number]

    def remove_card(self, card):
        return self.hand.remove(card)


class AllUsers(object):
    def __init__(self, player_list):
        self.players = player_list
        self.current_player = player_list[0]
        self.current_player_index = 0

    """ Since special cards directly affect player / player sequence"""
    def next_player(self, card):

        # Conditions for normal cards
        if card.number > 0:
            if self.current_player_index + 1 > (len(self.players) - 1):
                self.current_player_index = 0
            else:
                self.current_player_index += 1

        # Conditions for special cards
        elif card.number < 0:
            """ Skip card """
            if card.number == -2:
                if self.current_player_index + 2 > (len(self.players) - 1):
                    self.current_player_index = self.current_player_index + 2 - (len(self.players))
                else:
                    self.current_player_index += 2

            elif card.number == -1:
                """ Reverse card """
                """ Reverse the player sequence with current player at index 0"""
                new_players = []
                append_index = self.current_player_index
                for i in range(len(self.players)):
                    new_players.append(self.players[append_index])
                    append_index -= 1
                    if append_index < 0:
                        append_index = len(self.players) - 1
                self.players = new_players
                self.current_player_index = 1
        self.current_player = self.players[self.current_player_index]

        return self.current_player



