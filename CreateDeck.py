def create_deck():
   deck = [];
   for i in range(10):
       for color in ['blue','green','red','yellow']:
           if i == 0:
               card  = StandardCards(color,i);
               deck.append(card);
           else:
               card = StandardCards(color,i);
               deck.append(card);
               card = StandardCards(color,i);
               deck.append(card);
   
   for i in range(4):
       card = WildCard();
       deck.append(card);

   for i in range(4):
       cards = WildCard(); 
       card.is_draw_4 = True;
       deck.append(card);
   return deck;
        deal_one_card(p4,deck)
