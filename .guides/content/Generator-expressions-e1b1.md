---------------------

<span>**Generator expressions**</span> are similar to list comprehensions, but with parentheses instead of square brackets:

    >>> g = (x**2 for x in range(5))
    >>> g
    <generator object <genexpr> at 0x7f4c45a786c0>

The result is a generator object that knows how to iterate through a sequence of values. But unlike a list comprehension, it does not compute the values all at once; it waits to be asked. The built-in function <span>next</span> gets the next value from the generator:

    >>> next(g)
    0
    >>> next(g)
    1

When you get to the end of the sequence, <span>next</span> raises a StopIteration exception. You can also use a <span>for</span> loop to iterate through the values:

    >>> for val in g:
    ...     print(val)
    4
    9
    16

The generator object keeps track of where it is in the sequence, so the <span>for</span> loop picks up where <span>next</span> left off. Once the generator is exhausted, it continues to raise <span>StopIteration</span>:

    >>> next(g)
    StopIteration

Generator expressions are often used with functions like <span>sum</span>, <span>max</span>, and <span>min</span>:

    >>> sum(x**2 for x in range(5))
    30

