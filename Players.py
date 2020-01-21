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
