import random

from Cards import NumberCards, SpecialCards


class Deck(object):
    colors = ["red", "blue", "green", "yellow"]
    cards = []

    def __init__(self):
        for i in range(80):
            card_types = [NumberCards.NumberCards(color=random.choice(self.colors), number=random.randint(0, 9)),
                          SpecialCards.Reverse(color=random.choice(self.colors)),
                          SpecialCards.Skip(color=random.choice(self.colors))]
            card = random.choice(card_types)
            print(card.color)
            self.cards.append(card)

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
