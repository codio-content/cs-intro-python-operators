--------------------

A tuple is a sequence of values. The values can be any type, and they are indexed by integers, so in that respect tuples are a lot like lists. The important difference is that tuples are immutable.

Syntactically, a tuple is a comma-separated list of values:

    >>> t = 'a', 'b', 'c', 'd', 'e'

Although it is not necessary, it is common to enclose tuples in parentheses:

    >>> t = ('a', 'b', 'c', 'd', 'e')

To create a tuple with a single element, you have to include a final comma:

    >>> t1 = 'a',
    >>> type(t1)
    <class 'tuple'>

A value in parentheses is not a tuple:

    >>> t2 = ('a')
    >>> type(t2)
    <class 'str'>

Another way to create a tuple is the built-in function <span>tuple</span>. With no argument, it creates an empty tuple:

    >>> t = tuple()
    >>> t
    ()

If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of the sequence:

    >>> t = tuple('lupins')
    >>> t
    ('l', 'u', 'p', 'i', 'n', 's')

Because <span>tuple</span> is the name of a built-in function, you should avoid using it as a variable name.

Most list operators also work on tuples. The bracket operator indexes an element:

    >>> t = ('a', 'b', 'c', 'd', 'e')
    >>> t[0]
    'a'

And the slice operator selects a range of elements.

    >>> t[1:3]
    ('b', 'c')

But if you try to modify one of the elements of the tuple, you get an error:

    >>> t[0] = 'A'
    TypeError: object doesn't support item assignment

Because tuples are immutable, you can’t modify the elements. But you can replace one tuple with another:

    >>> t = ('A',) + t[1:]
    >>> t
    ('A', 'b', 'c', 'd', 'e')

This statement makes a new tuple and then makes <span>t</span> refer to it.

The relational operators work with tuples and other sequences; Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next elements, and so on, until it finds elements that differ. Subsequent elements are not considered (even if they are really big).

    >>> (0, 1, 2) < (0, 3, 4)
    True
    >>> (0, 1, 2000000) < (0, 3, 4)
    True

