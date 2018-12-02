-----------------

Here is a `__str__` method for <span>Deck</span>:

    #inside class Deck:

        def __str__(self):
            res = []
            for card in self.cards:
                res.append(str(card))
            return '\n'.join(res)

This method demonstrates an efficient way to accumulate a large string: building a list of strings and then using the string method <span>join</span>. The built-in function <span>str</span> invokes the `__str__` method on each card and returns the string representation.

Since we invoke <span>join</span> on a newline character, the cards are separated by newlines. Here’s what the result looks like:

    >>> deck = Deck()
    >>> print(deck)
    Ace of Clubs
    2 of Clubs
    3 of Clubs
    ...
    10 of Spades
    Jack of Spades
    Queen of Spades
    King of Spades

Even though the result appears on 52 lines, it is one long string that contains newlines.

