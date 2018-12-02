-----------

Inheritance is the ability to define a new class that is a modified version of an existing class. As an example, let’s say we want a class to represent a “hand”, that is, the cards held by one player. A hand is similar to a deck: both are made up of a collection of cards, and both require operations like adding and removing cards.

A hand is also different from a deck; there are operations we want for hands that don’t make sense for a deck. For example, in poker we might compare two hands to see which one wins. In bridge, we might compute a score for a hand in order to make a bid.

This relationship between classes—similar, but different—lends itself to inheritance. To define a new class that inherits from an existing class, you put the name of the existing class in parentheses:

    class Hand(Deck):
        """Represents a hand of playing cards."""

This definition indicates that <span>Hand</span> inherits from <span>Deck</span>; that means we can use methods like `pop_card` and `add_card` for Hands as well as Decks.

When a new class inherits from an existing one, the existing one is called the <span>**parent**</span> and the new class is called the <span>**child**</span>.

In this example, <span>Hand</span> inherits `__init__` from <span>Deck</span>, but it doesn’t really do what we want: instead of populating the hand with 52 new cards, the init method for Hands should initialize <span>cards</span> with an empty list.

If we provide an init method in the <span>Hand</span> class, it overrides the one in the <span>Deck</span> class:

    # inside class Hand:

        def __init__(self, label=''):
            self.cards = []
            self.label = label

When you create a Hand, Python invokes this init method, not the one in <span>Deck</span>.

    >>> hand = Hand('new hand')
    >>> hand.cards
    []
    >>> hand.label
    'new hand'

The other methods are inherited from <span>Deck</span>, so we can use `pop_card` and `add_card` to deal a card:

    >>> deck = Deck()
    >>> card = deck.pop_card()
    >>> hand.add_card(card)
    >>> print(hand)
    King of Spades

A natural next step is to encapsulate this code in a method called `move_cards`:

    #inside class Deck:

        def move_cards(self, hand, num):
            for i in range(num):
                hand.add_card(self.pop_card())

`move_cards` takes two arguments, a Hand object and the number of cards to deal. It modifies both <span>self</span> and <span>hand</span>, and returns <span>None</span>.

In some games, cards are moved from one hand to another, or from a hand back to the deck. You can use `move_cards` for any of these operations: <span>self</span> can be either a Deck or a Hand, and <span>hand</span>, despite the name, can also be a <span>Deck</span>.

Inheritance is a useful feature. Some programs that would be repetitive without inheritance can be written more elegantly with it. Inheritance can facilitate code reuse, since you can customize the behavior of parent classes without having to modify them. In some cases, the inheritance structure reflects the natural structure of the problem, which makes the design easier to understand.

On the other hand, inheritance can make programs difficult to read. When a method is invoked, it is sometimes not clear where to find its definition. The relevant code may be spread across several modules. Also, many of the things that can be done using inheritance can be done as well or better without it.

