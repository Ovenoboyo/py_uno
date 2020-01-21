class User(object):
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def play_card(self, number: int):
        self.hand.pop(number)
        return self.hand[number]
