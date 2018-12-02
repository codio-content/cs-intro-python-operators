-------------

A segment of a string is called a <span>**slice**</span>. Selecting a slice is similar to selecting a character:

    >>> s = 'Monty Python'
    >>> s[0:5]
    'Monty'
    >>> s[6:12]
    'Python'

The operator returns the part of the string from the “n-eth” character to the “m-eth” character, including the first but excluding the last. This behavior is counterintuitive, but it might help to imagine the indices pointing <span>*between*</span> the characters, as in the Figure below.

![image](/.guides/img/banana.jpg)



If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string:

    >>> fruit = 'banana'
    >>> fruit[:3]
    'ban'
    >>> fruit[3:]
    'ana'

If the first index is greater than or equal to the second the result is an <span>**empty string**</span>, represented by two quotation marks:

    >>> fruit = 'banana'
    >>> fruit[3:3]
    ''

An empty string contains no characters and has length 0, but other than that, it is the same as any other string.

Continuing this example, what do you think <span>fruit[:]</span> means? Try it and see.

