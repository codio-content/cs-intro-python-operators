----------------------

I have focused on lists of tuples, but almost all of the examples in this chapter also work with lists of lists, tuples of tuples, and tuples of lists. To avoid enumerating the possible combinations, it is sometimes easier to talk about sequences of sequences.

In many contexts, the different kinds of sequences (strings, lists and tuples) can be used interchangeably. So how should you choose one over the others?

To start with the obvious, strings are more limited than other sequences because the elements have to be characters. They are also immutable. If you need the ability to change the characters in a string (as opposed to creating a new string), you might want to use a list of characters instead.

Lists are more common than tuples, mostly because they are mutable. But there are a few cases where you might prefer tuples:

1.  In some contexts, like a <span>return</span> statement, it is syntactically simpler to create a tuple than a list.

2.  If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.

3.  If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

Because tuples are immutable, they don’t provide methods like <span>sort</span> and <span>reverse</span>, which modify existing lists. But Python provides the built-in function <span>sorted</span>, which takes any sequence and returns a new list with the same elements in sorted order, and <span>reversed</span>, which takes a sequence and returns an iterator that traverses the list in reverse order.

