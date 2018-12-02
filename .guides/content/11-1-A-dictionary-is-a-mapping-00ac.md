-------------------------

A <span>**dictionary**</span> is like a list, but more general. In a list, the indices have to be integers; in a dictionary they can be (almost) any type.

A dictionary contains a collection of indices, which are called <span>**keys**</span>, and a collection of values. Each key is associated with a single value. The association of a key and a value is called a <span>**key-value pair**</span> or sometimes an <span>**item**</span>.

In mathematical language, a dictionary represents a <span>**mapping**</span> from keys to values, so you can also say that each key “maps to” a value. As an example, we’ll build a dictionary that maps from English to Spanish words, so the keys and the values are all strings.

The function <span>`dict`</span> creates a new dictionary with no items. Because <span>dict</span> is the name of a built-in function, you should avoid using it as a variable name.

    >>> eng2sp = dict()
    >>> eng2sp
    {}

The squiggly-brackets, `{}`, represent an empty dictionary. To add items to the dictionary, you can use square brackets:

    >>> eng2sp['one'] = 'uno'

This line creates an item that maps from the key `'one'` to the value `'uno'`. If we print the dictionary again, we see a key-value pair with a colon between the key and value:

    >>> eng2sp
    {'one': 'uno'}

This output format is also an input format. For example, you can create a new dictionary with three items:

    >>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

But if you print <span>eng2sp</span>, you might be surprised:

    >>> eng2sp
    {'one': 'uno', 'three': 'tres', 'two': 'dos'}

The order of the key-value pairs might not be the same. If you type the same example on your computer, you might get a different result. In general, the order of items in a dictionary is unpredictable.

But that’s not a problem because the elements of a dictionary are never indexed with integer indices. Instead, you use the keys to look up the corresponding values:

    >>> eng2sp['two']
    'dos'

The key `'two'` always maps to the value `'dos'` so the order of the items doesn’t matter.

If the key isn’t in the dictionary, you get an exception:

    >>> eng2sp['four']
    KeyError: 'four'

The <span>`len`</span> function works on dictionaries; it returns the number of key-value pairs:

    >>> len(eng2sp)
    3

The <span>`in`</span> operator works on dictionaries, too; it tells you whether something appears as a <span>*key*</span> in the dictionary (appearing as a value is not good enough).

    >>> 'one' in eng2sp
    True
    >>> 'uno' in eng2sp
    False

To see whether something appears as a value in a dictionary, you can use the method <span>`values`</span>, which returns a collection of values, and then use the <span>in</span> operator:

    >>> vals = eng2sp.values()
    >>> 'uno' in vals
    True

The <span>in</span> operator uses different algorithms for lists and dictionaries. For lists, it searches the elements of the list in order, as in Section 8.4. As the list gets longer, the search time gets longer in direct proportion.

For dictionaries, Python uses an algorithm called a <span>**hashtable**</span> that has a remarkable property: the <span>in</span> operator takes about the same amount of time no matter how many items are in the dictionary. I explain how that’s possible in Section B.4, but the explanation might not make sense until you’ve read a few more chapters.

