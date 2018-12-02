---------------

For built-in types, there are relational operators (<span>\<</span>, <span>\></span>, <span>==</span>, etc.) that compare values and determine when one is greater than, less than, or equal to another. For programmer-defined types, we can override the behavior of the built-in operators by providing a method named `__lt__`, which stands for “less than”.

`__lt__` takes two parameters, <span>self</span> and <span>other</span>, and returns <span>True</span> if <span>self</span> is strictly less than <span>other</span>.

The correct ordering for cards is not obvious. For example, which is better, the 3 of Clubs or the 2 of Diamonds? One has a higher rank, but the other has a higher suit. In order to compare cards, you have to decide whether rank or suit is more important.

The answer might depend on what game you are playing, but to keep things simple, we’ll make the arbitrary choice that suit is more important, so all of the Spades outrank all of the Diamonds, and so on.

With that decided, we can write `__lt__`:

    # inside class Card:

        def __lt__(self, other):
            # check the suits
            if self.suit < other.suit: return True
            if self.suit > other.suit: return False

            # suits are the same... check ranks
            return self.rank < other.rank

You can write this more concisely using tuple comparison:

    # inside class Card:

        def __lt__(self, other):
            t1 = self.suit, self.rank
            t2 = other.suit, other.rank
            return t1 < t2

As an exercise, write an `__lt__` method for Time objects. You can use tuple comparison, but you also might consider comparing integers.

