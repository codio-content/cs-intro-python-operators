----------------------

A string is a sequence of characters. You can access the characters one at a time with the bracket operator:

    >>> fruit = 'banana'
    >>> letter = fruit[1]

The second statement selects character number 1 from <span>fruit</span> and assigns it to <span>letter</span>.

The expression in brackets is called an <span>**index**</span>. The index indicates which character in the sequence you want (hence the name).

But you might not get what you expect:

    >>> letter
    'a'

For most people, the first letter of `'banana'` is <span>b</span>, not <span>a</span>. But for computer scientists, the index is an offset from the beginning of the string, and the offset of the first letter is zero.

    >>> letter = fruit[0]
    >>> letter
    'b'

So <span>b</span> is the 0th letter (“zero-eth”) of `'banana'`, <span>a</span> is the 1th letter (“one-eth”), and <span>n</span> is the 2th letter (“two-eth”).

As an index you can use an expression that contains variables and operators:

    >>> i = 1
    >>> fruit[i]
    'a'
    >>> fruit[i+1]
    'n'

But the value of the index has to be an integer. Otherwise you get:

    >>> letter = fruit[1.5]
    TypeError: string indices must be integers

