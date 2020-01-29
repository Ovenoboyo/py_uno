class PlaySpace(object):
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def can_play(self, card):
        if len(self.cards) > 0:
            if self.cards[len(self.cards) - 1].color == card.color or \
                    self.cards[len(self.cards) - 1].number == card.number:
                return True
            else:
                return False
        else:
            return True
