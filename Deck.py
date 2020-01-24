import random

from Cards import NumberCards, SpecialCards


class Deck(object):
    colors = ["red", "blue", "green", "yellow"]
    cards = []

    def __init__(self):
        for i in range(60):
            for k in range(4):
                self.cards.append(SpecialCards.Reverse(color=self.colors[k]))
                self.cards.append(SpecialCards.Skip(color=self.colors[k]))
                for j in range(10):
                    self.cards.append(NumberCards.NumberCards(color=self.colors[k], number=j))

    def remove_card(self, card):
        self.cards.remove(card)

    def get_random_card(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def draw_top_card(self):
        card = self.cards[0]
        self.cards.remove(card)

        """ Add a card to the bottom of deck """
        card_types = [NumberCards.NumberCards(color=random.choice(self.colors), number=random.randint(0, 9)),
                      SpecialCards.Reverse(color=random.choice(self.colors)),
                      SpecialCards.Skip(color=random.choice(self.colors))]
        self.cards.append(random.choice(card_types))
        return card
