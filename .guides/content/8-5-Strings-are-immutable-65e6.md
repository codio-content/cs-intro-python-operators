---------------------

It is tempting to use the <span>[]</span> operator on the left side of an assignment, with the intention of changing a character in a string. For example:

    >>> greeting = 'Hello, world!'
    >>> greeting[0] = 'J'
    TypeError: 'str' object does not support item assignment

The “object” in this case is the string and the “item” is the character you tried to assign. For now, an object is the same thing as a value, but we will refine that definition later (Section 10.10).

The reason for the error is that strings are <span>**immutable**</span>, which means you can’t change an existing string. The best you can do is create a new string that is a variation on the original:

    >>> greeting = 'Hello, world!'
    >>> new_greeting = 'J' + greeting[1:]
    >>> new_greeting
    'Jello, world!'

This example concatenates a new first letter onto a slice of <span>greeting</span>. It has no effect on the original string.

