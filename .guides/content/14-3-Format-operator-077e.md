---------------

The argument of <span>write</span> has to be a string, so if we want to put other values in a file, we have to convert them to strings. The easiest way to do that is with <span>`str`</span>:

    >>> x = 52
    >>> fout.write(str(x))

An alternative is to use the <span>**format operator**</span>, <span>%</span>. When applied to integers, <span>%</span> is the modulus operator. But when the first operand is a string, <span>%</span> is the format operator.

The first operand is the <span>**format string**</span>, which contains one or more <span>**format sequences**</span>, which specify how the second operand is formatted. The result is a string.

For example, the format sequence `'%d'` means that the second operand should be formatted as a decimal integer:

    >>> camels = 42
    >>> '%d' % camels
    '42'

The result is the string `'42'`, which is not to be confused with the integer value <span>42</span>.

A format sequence can appear anywhere in the string, so you can embed a value in a sentence:

    >>> 'I have spotted %d camels.' % camels
    'I have spotted 42 camels.'

If there is more than one format sequence in the string, the second argument has to be a tuple. Each format sequence is matched with an element of the tuple, in order.

The following example uses `'%d'` to format an integer, `'%g'` to format a floating-point number, and `'%s'` to format a string:

    >>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
    'In 3 years I have spotted 0.1 camels.'

The number of elements in the tuple has to match the number of format sequences in the string. Also, the types of the elements have to match the format sequences:

    >>> '%d %d %d' % (1, 2)
    TypeError: not enough arguments for format string
    >>> '%d' % 'dollars'
    TypeError: %d format: a number is required, not str

In the first example, there aren’t enough elements; in the second, the element is the wrong type.

For more information on the format operator, see <https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting>. A more powerful alternative is the string format method, which you can read about at <https://docs.python.org/3/library/stdtypes.html#str.format>.

