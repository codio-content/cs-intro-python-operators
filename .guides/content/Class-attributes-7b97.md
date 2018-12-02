----------------

In order to print Card objects in a way that people can easily read, we need a mapping from the integer codes to the corresponding ranks and suits. A natural way to do that is with lists of strings. We assign these lists to <span>**class attributes**</span>:

    # inside class Card:

        suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
                  '8', '9', '10', 'Jack', 'Queen', 'King']

        def __str__(self):
            return '%s of %s' % (Card.rank_names[self.rank],
                                 Card.suit_names[self.suit])

Variables like `suit_names` and `rank_names`, which are defined inside a class but outside of any method, are called class attributes because they are associated with the class object <span>Card</span>.

This term distinguishes them from variables like <span>suit</span> and <span>rank</span>, which are called <span>**instance attributes**</span> because they are associated with a particular instance.

Both kinds of attribute are accessed using dot notation. For example, in `__str__`, <span>self</span> is a Card object, and <span>self.rank</span> is its rank. Similarly, <span>Card</span> is a class object, and `Card.rank_names` is a list of strings associated with the class.

Every card has its own <span>suit</span> and <span>rank</span>, but there is only one copy of `suit_names` and `rank_names`.

Putting it all together, the expression `Card.rank_names[self.rank]` means “use the attribute <span>rank</span> from the object <span>self</span> as an index into the list `rank_names` from the class <span>Card</span>, and select the appropriate string.”

The first element of `rank_names` is <span>None</span> because there is no card with rank zero. By including <span>None</span> as a place-keeper, we get a mapping with the nice property that the index 2 maps to the string `'2'`, and so on. To avoid this tweak, we could have used a dictionary instead of a list.

With the methods we have so far, we can create and print cards:

    >>> card1 = Card(2, 11)
    >>> print(card1)
    Jack of Hearts

![image](/.guides/img/card1.jpg)



Figure  is a diagram of the <span>Card</span> class object and one Card instance. <span>Card</span> is a class object; its type is <span>type</span>. <span>card1</span> is an instance of <span>Card</span>, so its type is <span>Card</span>. To save space, I didn’t draw the contents of `suit_names` and `rank_names`.

