import random

from Cards import NumberCards, SpecialCards


class Deck(object):
    colors = ["red", "blue", "green", "yellow"]
    cards = []

    def __init__(self):
        for i in range(60):
            card_types = [NumberCards.NumberCards(color=random.choice(self.colors), number=random.randint(0, 9)),
                          SpecialCards.Reverse(color=random.choice(self.colors)),
                          SpecialCards.Skip(color=random.choice(self.colors))]
            card = random.choice(card_types)
            self.cards.append(card)

            for i in range(4):
                card = WildCard();
                deck.append(card);

            for i in range(4):
                cards = WildCard();
                card.is_draw_4 = True;
                deck.append(card);
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
