------------

There are fifty-two cards in a deck, each of which belongs to one of four suits and one of thirteen ranks. The suits are Spades, Hearts, Diamonds, and Clubs (in descending order in bridge). The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Depending on the game that you are playing, an Ace may be higher than King or lower than 2.

If we want to define a new object to represent a playing card, it is obvious what the attributes should be: <span>rank</span> and <span>suit</span>. It is not as obvious what type the attributes should be. One possibility is to use strings containing words like `'Spade'` for suits and `'Queen'` for ranks. One problem with this implementation is that it would not be easy to compare cards to see which had a higher rank or suit.

An alternative is to use integers to <span>**encode**</span> the ranks and suits. In this context, “encode” means that we are going to define a mapping between numbers and suits, or between numbers and ranks. This kind of encoding is not meant to be a secret (that would be “encryption”).

For example, this table shows the suits and the corresponding integer codes:

  ---------- ------------------------ ---
  Spades      <span>$\mapsto$</span>  3
  Hearts      <span>$\mapsto$</span>  2
  Diamonds    <span>$\mapsto$</span>  1
  Clubs       <span>$\mapsto$</span>  0
  ---------- ------------------------ ---

This code makes it easy to compare cards; because higher suits map to higher numbers, we can compare suits by comparing their codes.

The mapping for ranks is fairly obvious; each of the numerical ranks maps to the corresponding integer, and for face cards:

  ------- ------------------------ ----
  Jack     <span>$\mapsto$</span>  11
  Queen    <span>$\mapsto$</span>  12
  King     <span>$\mapsto$</span>  13
  ------- ------------------------ ----

I am using the <span>$\mapsto$</span> symbol to make it clear that these mappings are not part of the Python program. They are part of the program design, but they don’t appear explicitly in the code.

The class definition for <span>Card</span> looks like this:

    class Card:
        """Represents a standard playing card."""

        def __init__(self, suit=0, rank=2):
            self.suit = suit
            self.rank = rank

As usual, the init method takes an optional parameter for each attribute. The default card is the 2 of Clubs.

To create a Card, you call <span>Card</span> with the suit and rank of the card you want.

    queen_of_diamonds = Card(1, 12)

