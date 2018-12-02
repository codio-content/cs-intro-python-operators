-----------------------------

To deal cards, we would like a method that removes a card from the deck and returns it. The list method <span>pop</span> provides a convenient way to do that:

    #inside class Deck:

        def pop_card(self):
            return self.cards.pop()

Since <span>pop</span> removes the <span>*last*</span> card in the list, we are dealing from the bottom of the deck.

To add a card, we can use the list method <span>append</span>:

    #inside class Deck:

        def add_card(self, card):
            self.cards.append(card)

A method like this that uses another method without doing much work is sometimes called a <span>**veneer**</span>. The metaphor comes from woodworking, where a veneer is a thin layer of good quality wood glued to the surface of a cheaper piece of wood to improve the appearance.

In this case `add_card` is a “thin” method that expresses a list operation in terms appropriate for decks. It improves the appearance, or interface, of the implementation.

As another example, we can write a Deck method named <span>shuffle</span> using the function <span>shuffle</span> from the <span>random</span> module:

    # inside class Deck:
                
        def shuffle(self):
            random.shuffle(self.cards)

Don’t forget to import <span>random</span>.

As an exercise, write a Deck method named <span>sort</span> that uses the list method <span>sort</span> to sort the cards in a <span>Deck</span>. <span>sort</span> uses the `__lt__` method we defined to determine the order.

